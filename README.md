# ⚡ FastAPI CRUD API with PostgreSQL, Alembic & JWT Auth

Welcome to my end-to-end **FastAPI** project! This repository is the product of following the [17+ hour FastAPI course](https://www.youtube.com/watch?v=0sOvCWFmrtA) by freeCodeCamp.org. It showcases everything I've learned about building scalable, secure, and production-ready APIs in Python — from basic routing to Docker and CI/CD!

---

## 🚀 What I Built

This project is a fully-featured **REST API** built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, with authentication, authorization, Alembic migrations, Docker deployment, and even GitHub Actions for CI/CD.

### 🧠 Key Concepts Covered

✅ Path Operations with FastAPI  
✅ Pydantic for Request & Response Validation  
✅ SQLAlchemy ORM with PostgreSQL  
✅ Alembic for Database Migrations  
✅ OAuth2 and JWT Token Authentication  
✅ Dependency Injection  
✅ SQL Joins & Relationships  
✅ Docker & Docker Compose  
✅ NGINX & Gunicorn for Production  
✅ CI/CD with GitHub Actions  
✅ Unit Testing with Pytest & Fixtures  
✅ PostgreSQL in Production on Heroku & Ubuntu VM

---

## 🛠️ Tech Stack

| Layer         | Tech Used                             |
| ------------- | ------------------------------------- |
| API Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| ORM           | SQLAlchemy                            |
| DB            | PostgreSQL                            |
| Migrations    | Alembic                               |
| Auth          | OAuth2 + JWT                          |
| Testing       | Pytest + TestClient                   |
| CI/CD         | GitHub Actions                        |
| Container     | Docker, Docker Compose                |
| Web Server    | NGINX + Gunicorn                      |
| Deployment    | Heroku, Ubuntu                        |

---

## 📦 Features

- ✅ **User registration & login**
- 🔐 **JWT token-based authentication**
- 📝 **CRUD operations for posts**
- 👥 **User-Post ownership and authorization**
- ❤️ **Voting (likes) system**
- 📑 **Auto-generated Swagger & Redoc API docs**
- 🧪 **Robust Pytest test suite with DB mocking**
- 🚀 **Production deployment on Heroku & Ubuntu**
- 🔄 **GitHub Actions CI/CD pipeline**
- 🐳 **Dockerized app with containerized PostgreSQL**

---

## 📁 Project Structure

```
app/
├── main.py           # FastAPI entrypoint
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── database.py       # DB connection
├── routers/          # Route files (posts, users, auth, vote)
├── oauth2.py         # JWT token logic
├── config.py         # Settings via Pydantic + .env
alembic/              # Alembic migration scripts
tests/                # Pytest test files
Dockerfile            # For containerizing the app
docker-compose.yml    # For local container orchestration
```

---

## 🧪 Running Locally

### Clone the Repo:

```bash
git clone https://github.com/yourusername/fastapi-course-project.git
cd fastapi-course-project
```

### Create & Activate Virtual Env:

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Setup Environment:

Create a `.env` file:

```env
DATABASE_HOSTNAME=yourHostName
DATABASE_PORT=yourPort
DATABASE_PASSWORD=yourPassword
DATABASE_NAME=yourDatabaseName
DATABASE_USERNAME=yourUsername
SECRET_KEY=supersecret
ALGORITHM=yourAlgorithm
ACCESS_TOKEN_EXPIRE_MINUTES=yourTokenExpiriationTime
```

### Run Migrations:

```bash
alembic upgrade head
```

### Start the App:

```bash
uvicorn app.main:app --reload
```

### Visit the API docs at:

- 📜 Swagger UI → http://localhost:8000/docs (on your machine)
- 📘 ReDoc → http://localhost:8000/redoc (on your machine)

---

## 🐳 Docker (Optional)

To run using Docker and Docker Compose:

```bash
docker-compose up --build
```

---

## 🌍 Deployed Demo

🔗 Coming Soon: https://your-live-url.com

---

## ✅ What I Learned

This course helped me learn and apply:

- Clean architecture for scalable backend APIs
- Deep understanding of request validation, routing, and auth
- Full DB management using Alembic & PostgreSQL
- Test-driven backend development
- Building and deploying real apps with Docker, Heroku, and GitHub Actions

---

## 🙋‍♂️ About Me

Hi, I'm Sarbojit Biswas — a B.Tech CSE (AI/ML) student who loves building real-world backend systems! This project marks a huge milestone in my learning path, and I'm excited to share it with recruiters, collaborators, and friends 🚀

---
