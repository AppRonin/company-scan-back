# 🧠 Company Scan - Backend API

Backend service for **Company Scan**, built with **Django**, **DRF**, **Dramatiq**, and **Redis**.  
It powers the web automation system used by the Flutter frontend.

---

## ⚙️ Tech Stack

- 🐍 **Django** – Core web framework
- ⚡ **Django REST Framework (DRF)** – RESTful API support
- 🎭 **Dramatiq** – Background task processing
- 🧩 **Redis** – Message broker and caching layer

---

## 🚀 Setup

### 1️⃣ Clone the repo

```bash
git clone https://github.com/AppRonin/company-scan-backend.git
cd company-scan-backend
```

### 2️⃣ Create a virtual environment

```bash
python -m venv env
source env/bin/activate
```

### 3️⃣ Create a `.env` file

```
SECRET_KEY=your_secret_key
DEBUG=True
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run Redis

```bash
redis-server
```

### 6️⃣ Start Dramatiq worker

```bash
dramatiq yourapp.tasks
```

### 7️⃣ Run the API server

```bash
python manage.py runserver
```

---

## 🧑‍🏭 Author

**AppRonin**

---
