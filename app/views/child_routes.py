"""
Module: child_routes
Description: API routes for children management
Author: Student
Date: 2025-10-23
"""

from fastapi import APIRouter, HTTPException, status
from app.controllers.child_controller import ChildController
from app.models.child_model import ChildModel, ChildCreate, ChildUpdate, MultipleChildrenCreate
from typing import List, Optional, Dict, Any

# Initialize router without prefix (it's already set in main.py)
router = APIRouter(prefix="/children", tags=["children"])

# Initialize controller
childController = ChildController()


@router.post("/", response_model=ChildModel, status_code=status.HTTP_201_CREATED)
def create_child(payload: ChildCreate):
    """
    Create a new child
    
    Args:
        payload: Child creation data
        
    Returns:
        ChildModel: Created child
    """
    return childController.createChild(payload.name, payload.age, payload.grade)


@router.post("/batch/", response_model=List[ChildModel], status_code=status.HTTP_201_CREATED)
def create_multiple_children(payload: MultipleChildrenCreate):
    """
    Create multiple children at once
    
    Args:
        payload: List of children to create
        
    Returns:
        List[ChildModel]: List of created children
    """
    children_data = [
        {"name": child.name, "age": child.age, "grade": child.grade}
        for child in payload.children
    ]
    return childController.createMultipleChildren(children_data)


@router.get("/", response_model=List[ChildModel])
def get_all_children():
    """
    Get all children
    
    Returns:
        List[ChildModel]: List of all children
    """
    return childController.getAllChildren()


@router.get("/{child_id}", response_model=ChildModel)
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


@router.put("/{child_id}", response_model=ChildModel)
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


@router.delete("/{child_id}", status_code=status.HTTP_204_NO_CONTENT)
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


@router.get("/age-distribution/{range_step}", response_model=Dict[str, Any])
def get_age_distribution(range_step: int = 1):
    """
    Get the distribution of children by age ranges
    
    Args:
        range_step (int, optional): Size of the age range. Default: 1.
                                  - If 1: ranges will be 0-1, 1-2, 2-3, etc.
                                  - If 2: ranges will be 0-2, 2-4, 4-6, etc.
                                  - If 3: ranges will be 0-3, 3-6, 6-9, etc.
    
    Returns:
        dict: {
            "total_children": int,  # Total number of children in the system
            "age_distribution": [
                {
                    "range": "{start}-{end}",  # Age range
                    "count": int  # Number of children in this range
                },
                ...
            ]
        }
        
    Example response (range_step=1):
        {
            "total_children": 15,
            "age_distribution": [
                {"range": "0-1", "count": 2},
                {"range": "1-2", "count": 3},
                {"range": "2-3", "count": 5},
                {"range": "3-4", "count": 3},
                {"range": "4-5", "count": 2}
            ]
        }
        
    Example response (range_step=2):
        {
            "total_children": 15,
            "age_distribution": [
                {"range": "0-2", "count": 5},
                {"range": "2-4", "count": 8},
                {"range": "4-6", "count": 2}
            ]
        }
    """
    if range_step <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Range step must be a positive integer"
        )
    
    try:
        return childController.get_age_distribution(range_step)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error calculating age distribution: {str(e)}"
        )
