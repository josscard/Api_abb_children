"""
Module: child_model
Description: Child data entity
Author: Student
Date: 2025-10-23
"""

from pydantic import BaseModel
from typing import Optional


class ChildModel(BaseModel):
    """Child data structure"""
    
    id: int
    name: str
    age: int
    grade: str


class ChildCreate(BaseModel):
    """
    Child creation request model
    """
    
    name: str
    age: int
    grade: str


class ChildUpdate(BaseModel):
    """
    Child update request model
    """
    
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[str] = None
