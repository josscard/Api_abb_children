---
description: Create api kids with tree binary
---

# FastAPI CRUD Children with BST - PyCharm Workflow

## Project Structure
```
children_api/
├── main.py
├── requirements.txt
├── .env
└── app/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    │   ├── child_model.py
    │   └── tree_node.py
    ├── controllers/
    │   ├── __init__.py
    │   └── child_controller.py
    └── views/
        ├── __init__.py
        └── child_routes.py
```

---

## 1. requirements.txt
```txt
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
```

---

## 2. app/models/child_model.py
```python
"""
Module: child_model
Description: Child data entity
Author: Student
Date: 2025-10-23
"""

from pydantic import BaseModel


class ChildModel(BaseModel):
    """Child data structure"""
    
    id: int
    name: str
    age: int
    grade: str
```

---

## 3. app/models/tree_node.py
```python
"""
Module: tree_node
Description: Binary Search Tree node
Author: Student
Date: 2025-10-23
"""

from app.models.child_model import ChildModel


class TreeNode:
    """Node for Binary Search Tree"""
    
    def __init__(self, child: ChildModel):
        """
        Initialize tree node
        
        Args:
            child: ChildModel instance
        """
        self.child = child
        self.left = None
        self.right = None
```

---

## 4. app/controllers/child_controller.py
```python
"""
Module: child_controller
Description: Business logic for children management using BST
Author: Student
Date: 2025-10-23
"""

from app.models.child_model import ChildModel
from app.models.tree_node import TreeNode


class ChildController:
    """Controller for children CRUD operations"""
    
    def __init__(self):
        """Initialize controller with empty tree"""
        self._root = None
        self._nextId = 1
    
    def createChild(self, name: str, age: int, grade: str) -> ChildModel:
        """
        Create new child and insert into BST
        
        Args:
            name: Child's name
            age: Child's age
            grade: Child's grade
            
        Returns:
            ChildModel: Created child
        """
        # Create child with auto-increment ID
        newChild = ChildModel(
            id=self._nextId,
            name=name,
            age=age,
            grade=grade
        )
        self._nextId = self._nextId + 1
        
        # Insert into BST
        self._root = self._insertNode(self._root, newChild)
        
        return newChild
    
    def _insertNode(self, node: TreeNode, child: ChildModel) -> TreeNode:
        """
        Recursive insertion into BST (by ID)
        
        Args:
            node: Current node
            child: Child to insert
            
        Returns:
            TreeNode: Updated node
        """
        # Base case: empty spot found
        if node is None:
            return TreeNode(child)
        
        # Compare IDs and go left or right
        if child.id < node.child.id:
            node.left = self._insertNode(node.left, child)
        else:
            node.right = self._insertNode(node.right, child)
        
        return node
    
    def getChildById(self, childId: int) -> ChildModel:
        """
        Search child by ID in BST
        
        Args:
            childId: Child ID to search
            
        Returns:
            ChildModel: Found child or None
        """
        return self._searchNode(self._root, childId)
    
    def _searchNode(self, node: TreeNode, childId: int) -> ChildModel:
        """
        Recursive search in BST
        
        Args:
            node: Current node
            childId: ID to search
            
        Returns:
            ChildModel: Found child or None
        """
        # Base case: not found
        if node is None:
            return None
        
        # Found
        if node.child.id == childId:
            return node.child
        
        # Search left or right
        if childId < node.child.id:
            return self._searchNode(node.left, childId)
        else:
            return self._searchNode(node.right, childId)
    
    def getAllChildren(self) -> list:
        """
        Get all children in order (inorder traversal)
        
        Returns:
            list: List of ChildModel objects
        """
        result = []
        self._inorderTraversal(self._root, result)
        return result
    
    def _inorderTraversal(self, node: TreeNode, result: list) -> None:
        """
        Inorder traversal (left, root, right)
        
        Args:
            node: Current node
            result: List to store children
        """
        if node is not None:
            self._inorderTraversal(node.left, result)
            result.append(node.child)
            self._inorderTraversal(node.right, result)
    
    def updateChild(self, childId: int, name: str, age: int, grade: str) -> ChildModel:
        """
        Update child data
        
        Args:
            childId: Child ID
            name: New name
            age: New age
            grade: New grade
            
        Returns:
            ChildModel: Updated child or None
        """
        child = self.getChildById(childId)
        
        if child is None:
            return None
        
        # Update fields (ID stays the same)
        child.name = name
        child.age = age
        child.grade = grade
        
        return child
    
    def deleteChild(self, childId: int) -> bool:
        """
        Delete child from BST
        
        Args:
            childId: Child ID to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        # Check if exists
        if self.getChildById(childId) is None:
            return False
        
        # Delete from tree
        self._root = self._deleteNode(self._root, childId)
        return True
    
    def _deleteNode(self, node: TreeNode, childId: int) -> TreeNode:
        """
        Recursive deletion from BST
        
        Args:
            node: Current node
            childId: ID to delete
            
        Returns:
            TreeNode: Updated node
        """
        if node is None:
            return None
        
        # Search for node to delete
        if childId < node.child.id:
            node.left = self._deleteNode(node.left, childId)
        elif childId > node.child.id:
            node.right = self._deleteNode(node.right, childId)
        else:
            # Node found - handle 3 cases
            
            # Case 1: No children (leaf)
            if node.left is None and node.right is None:
                return None
            
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Case 3: Two children
            # Find minimum in right subtree
            minNode = self._findMin(node.right)
            node.child = minNode.child
            node.right = self._deleteNode(node.right, minNode.child.id)
        
        return node
    
    def _findMin(self, node: TreeNode) -> TreeNode:
        """
        Find minimum node (leftmost)
        
        Args:
            node: Starting node
            
        Returns:
            TreeNode: Minimum node
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
```

---

## 5. app/views/child_routes.py
```python
"""
Module: child_routes
Description: FastAPI endpoints for children
Author: Student
Date: 2025-10-23
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.controllers.child_controller import ChildController


router = APIRouter(prefix="/children", tags=["Children"])
controller = ChildController()


class ChildCreateRequest(BaseModel):
    """Request body for creating child"""
    name: str
    age: int
    grade: str


class ChildUpdateRequest(BaseModel):
    """Request body for updating child"""
    name: str
    age: int
    grade: str


@router.post("/")
def createChild(request: ChildCreateRequest):
    """
    Create new child
    
    Args:
        request: Child data
        
    Returns:
        Created child
    """
    child = controller.createChild(request.name, request.age, request.grade)
    return {"success": True, "data": child}


@router.get("/{childId}")
def getChild(childId: int):
    """
    Get child by ID
    
    Args:
        childId: Child ID
        
    Returns:
        Child data
    """
    child = controller.getChildById(childId)
    
    if child is None:
        raise HTTPException(status_code=404, detail="Child not found")
    
    return {"success": True, "data": child}


@router.get("/")
def getAllChildren():
    """
    Get all children sorted by ID
    
    Returns:
        List of children
    """
    children = controller.getAllChildren()
    return {"success": True, "data": children, "count": len(children)}


@router.put("/{childId}")
def updateChild(childId: int, request: ChildUpdateRequest):
    """
    Update child data
    
    Args:
        childId: Child ID
        request: Updated data
        
    Returns:
        Updated child
    """
    child = controller.updateChild(childId, request.name, request.age, request.grade)
    
    if child is None:
        raise HTTPException(status_code=404, detail="Child not found")
    
    return {"success": True, "data": child}


@router.delete("/{childId}")
def deleteChild(childId: int):
    """
    Delete child
    
    Args:
        childId: Child ID
        
    Returns:
        Success message
    """
    deleted = controller.deleteChild(childId)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="Child not found")
    
    return {"success": True, "message": "Child deleted"}
```

---

## 6. app/__init__.py
```python
"""App package"""
```

---

## 7. main.py
```python
"""
Module: main
Description: FastAPI application entry point
Author: Student
Date: 2025-10-23
"""

from fastapi import FastAPI
from app.views.child_routes import router as childRouter


app = FastAPI(title="Children API", version="1.0.0")

# Register routes
app.include_router(childRouter)


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Children API with BST", "status": "running"}
```

---

## Installation Steps

### 1. Create project
```bash
mkdir children_api
cd children_api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run server
```bash
uvicorn main:app --reload
```

### 4. Test API
Open: `http://localhost:8000/docs`

---

## Usage Examples (Swagger UI)

### POST /children/
```json
{
  "name": "John Doe",
  "age": 8,
  "grade": "3rd"
}
```

### GET /children/
Returns all children sorted by ID

### GET /children/1
Returns child with ID 1

### PUT /children/1
```json
{
  "name": "John Smith",
  "age": 9,
  "grade": "4th"
}
```

### DELETE /children/1
Deletes child with ID 1

---

## BST Characteristics

- **Insertion**: O(log n) average, O(n) worst case
- **Search**: O(log n) average, O(n) worst case
- **Deletion**: O(log n) average, O(n) worst case
- **Inorder traversal**: Returns children sorted by ID
- **Auto-increment ID**: Guarantees tree order

---

## Important Notes

1. Tree is ordered by ID (auto-incremental)
2. Tree exists only in memory (lost on restart)
3. For persistence, add database
4. Follows all rules: camelCase, no lambdas, docstrings
5. Simple and readable code for 4th semester