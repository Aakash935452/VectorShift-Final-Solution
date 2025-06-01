# 🚀 VectorShift Final Solution

This repository contains the final solution to the **VectorShift Frontend Developer Assessment**. It includes a complete implementation of a dynamic node editor with full backend integration using FastAPI and a frontend built with React and Tailwind CSS.

---

## 📁 Project Structure


---

## 🧰 Tech Stack

### 🖥️ Frontend
- **React**
- **Vite**
- **Tailwind CSS**
- **Framer Motion**
- **ShadCN UI**
- **Lucide Icons**
- **Zustand** (state management)
- **UUID**
- **React Toastify**

### ⚙️ Backend
- **FastAPI**
- **Python 3.12**
- **Uvicorn**
- **Pydantic**

---

## ⚙️ Setup Instructions

### 🔧 Backend (FastAPI)
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate  # For macOS/Linux
pip install -r requirements.txt
uvicorn main:app --reload
