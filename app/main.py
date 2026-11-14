
from fastapi import FastAPI

from app.database import engine, Base
from app import models

from app.routes.users import router as users_router
from app.auth import router as auth_router
from app.routes.items import router as items_router


# Create database tables
Base.metadata.create_all(bind=engine)


# Initialize FastAPI
app = FastAPI(
    title="Secure FastAPI Microservice",
    description="API with SQLite, JWT Authentication and Secure CRUD",
    version="1.0.0"
)


# Register API routers
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(items_router)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Secure FastAPI Microservice",
        "status": "Running successfully"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
