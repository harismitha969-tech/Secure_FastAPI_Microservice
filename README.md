# 🔐 Secure FastAPI Microservice

## Project Overview

Secure FastAPI Microservice is a RESTful API application developed using Python and FastAPI. It provides secure user registration, authentication using JWT (JSON Web Tokens), and CRUD (Create, Read, Update, Delete) operations for managing items.

The project focuses on API security, authentication, database integration, and efficient backend development.

## 🚀 Features

- User Registration
- Secure Password Hashing
- User Login and Authentication
- JWT Token-Based Authentication
- Protected API Endpoints
- Create Items
- Read Items
- Update Items
- Delete Items
- Database Integration
- Interactive API Documentation using Swagger UI

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLite
- SQLAlchemy
- Pydantic
- JWT Authentication
- Swagger UI

## 📁 Project Structure

```text
Secure_FastAPI_Microservice/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── items.py
│       ├── users.py
│       └── tests/
│           └── test_api.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/harismitha969-tech/Secure_FastAPI_Microservice.git
```

### 2. Navigate to Project Directory

```bash
cd Secure_FastAPI_Microservice
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

## 🌐 API Documentation

After starting the server, open:

**Swagger UI:**

http://127.0.0.1:8000/docs

**ReDoc:**

http://127.0.0.1:8000/redoc

## 🔑 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/register` | Register a new user |
| POST | `/auth/login` | User login |
| POST | `/items/` | Create an item |
| GET | `/items/` | Get all items |
| PUT | `/items/{item_id}` | Update an item |
| DELETE | `/items/{item_id}` | Delete an item |

## 🔒 Authentication

The application uses JWT (JSON Web Token) authentication to secure protected API endpoints.

Steps:

1. Register a new user.
2. Login using registered credentials.
3. Obtain the JWT access token.
4. Click the Authorize button in Swagger UI.
5. Enter the access token.
6. Access protected API endpoints.

## 🧪 Testing

The API can be tested using:

- Swagger UI
- FastAPI TestClient
- Pytest (if configured)

## 🎯 Learning Outcomes

- Understanding REST API development.
- Implementing JWT authentication.
- Password hashing and security.
- Database connectivity.
- CRUD operations.
- Building secure backend applications using FastAPI.

## 👨‍💻 Author

**GitHub:** [harismitha969-tech](https://github.com/harismitha969-tech)

**Project:** Secure FastAPI Microservice

---

⭐ If you find this project useful, consider giving it a star on GitHub.
