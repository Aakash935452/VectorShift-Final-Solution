
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS settings for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input format from frontend
class PipelineData(BaseModel):
    nodes: list
    edges: list

@app.post("/pipelines/parse")
async def parse_pipeline(data: PipelineData):
    node_ids = {node['id'] for node in data.nodes}
    edge_list = [(edge['source'], edge['target']) for edge in data.edges]

    def is_dag(n, edges):
        from collections import defaultdict, deque
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([node for node in node_ids if indegree[node] == 0])
        visited = 0

        while queue:
            current = queue.popleft()
            visited += 1
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == len(node_ids)

    return {
        "num_nodes": len(data.nodes),
        "num_edges": len(data.edges),
        "is_dag": is_dag(len(data.nodes), edge_list)
    }
