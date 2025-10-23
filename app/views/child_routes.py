"""
Module: child_routes
Description: API routes for children management
Author: Student
Date: 2025-10-23
"""

from fastapi import APIRouter, HTTPException, status
from app.controllers.child_controller import ChildController
from app.models.child_model import ChildModel, ChildCreate, ChildUpdate
from typing import List, Optional

# Initialize router
router = APIRouter()

# Initialize controller
childController = ChildController()


@router.post("/children/", response_model=ChildModel, status_code=status.HTTP_201_CREATED)
def create_child(payload: ChildCreate):
    """
    Create a new child
    
    Args:
        payload: Child creation data
        
    Returns:
        ChildModel: Created child
    """
    return childController.createChild(payload.name, payload.age, payload.grade)


@router.get("/children/", response_model=List[ChildModel])
def get_all_children():
    """
    Get all children
    
    Returns:
        List[ChildModel]: List of all children
    """
    return childController.getAllChildren()


@router.get("/children/{child_id}", response_model=ChildModel)
def get_child(child_id: int):
    """
    Get child by ID
    
    Args:
        child_id: ID of the child to retrieve
        
    Returns:
        ChildModel: Requested child
        
    Raises:
        HTTPException: If child not found
    """
    child = childController.getChildById(child_id)
    if child is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found"
        )
    return child


@router.put("/children/{child_id}", response_model=ChildModel)
def update_child(child_id: int, payload: ChildUpdate):
    """
    Update child information
    
    Args:
        child_id: ID of the child to update
        payload: Child update data (all fields optional)
        
    Returns:
        ChildModel: Updated child
        
    Raises:
        HTTPException: If child not found
    """
    updated_child = childController.updateChild(
        childId=child_id,
        name=payload.name,
        age=payload.age,
        grade=payload.grade
    )
    
    if updated_child is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found"
        )
        
    return updated_child


@router.delete("/children/{child_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_child(child_id: int):
    """
    Delete a child by ID
    
    Args:
        child_id: ID of the child to delete
        
    Raises:
        HTTPException: If child not found
    """
    success = childController.deleteChild(child_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found"
        )
