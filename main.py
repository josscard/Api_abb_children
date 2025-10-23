"""
Module: main
Description: Main application entry point
Author: Student
Date: 2025-10-23
"""

from fastapi import FastAPI
from app.views import child_routes

# Initialize FastAPI app
app = FastAPI(
    title="Children Management API",
    description="API for managing children using Binary Search Tree",
    version="1.0.0"
)

# Include routes
app.include_router(child_routes.router, prefix="/api", tags=["children"])


@app.get("/")
def read_root():
    """
    Root endpoint
    
    Returns:
        dict: Welcome message
    """
    return {
        "message": "Welcome to the Children Management API",
        "docs": "/docs"
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
