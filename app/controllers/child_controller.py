"""
Module: child_controller
Description: Business logic for children management using BST
Author: Student
Date: 2025-10-23
"""

from typing import List, Optional
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
        
    def createMultipleChildren(self, children_data: list[dict]) -> list[ChildModel]:
        """
        Create multiple children and insert them into BST
        
        Args:
            children_data: List of dictionaries with child data (name, age, grade)
            
        Returns:
            list[ChildModel]: List of created children
        """
        created_children = []
        for child_data in children_data:
            new_child = self.createChild(
                name=child_data['name'],
                age=child_data['age'],
                grade=child_data['grade']
            )
            created_children.append(new_child)
            
        return created_children
    
    def _insertNode(self, node: Optional[TreeNode], child: ChildModel) -> TreeNode:
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
    
    def getChildById(self, childId: int) -> Optional[ChildModel]:
        """
        Search child by ID in BST
        
        Args:
            childId: Child ID to search
            
        Returns:
            ChildModel: Found child or None
        """
        return self._searchNode(self._root, childId)
    
    def _searchNode(self, node: Optional[TreeNode], childId: int) -> Optional[ChildModel]:
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
    
    def getAllChildren(self) -> List[ChildModel]:
        """
        Get all children using in-order traversal
        
        Returns:
            List[ChildModel]: List of all children
        """
        result = []
        self._inOrderTraversal(self._root, result)
        return result
    
    def _inOrderTraversal(self, node: Optional[TreeNode], result: List[ChildModel]):
        """
        In-order traversal of BST (left-root-right)
        
        Args:
            node: Current node
            result: List to store results
        """
        if node is not None:
            self._inOrderTraversal(node.left, result)
            result.append(node.child)
            self._inOrderTraversal(node.right, result)
    
    def updateChild(self, childId: int, name: str = None, age: int = None, grade: str = None) -> Optional[ChildModel]:
        """
        Update child information
        
        Args:
            childId: ID of child to update
            name: New name (optional)
            age: New age (optional)
            grade: New grade (optional)
            
        Returns:
            ChildModel: Updated child or None if not found
        """
        node = self._findNode(self._root, childId)
        if node is None:
            return None
        
        # Update fields if provided
        if name is not None:
            node.child.name = name
        if age is not None:
            node.child.age = age
        if grade is not None:
            node.child.grade = grade
            
        return node.child
    
    def _findNode(self, node: Optional[TreeNode], childId: int) -> Optional[TreeNode]:
        """
        Find node by ID
        
        Args:
            node: Current node
            childId: ID to find
            
        Returns:
            TreeNode: Found node or None
        """
        if node is None:
            return None
            
        if node.child.id == childId:
            return node
        if childId < node.child.id:
            return self._findNode(node.left, childId)
        else:
            return self._findNode(node.right, childId)
    
    def deleteChild(self, child_id: int) -> None:
        """
        Delete a child by ID
        
        Args:
            child_id: ID of the child to delete
            
        Raises:
            ValueError: If child not found
        """
        self.root = self._delete_node(self.root, child_id)
        
    def get_age_distribution(self, range_step: int = 1) -> dict:
        """
        Get the distribution of children by age ranges.
        Each child is counted in the first range that includes their age.
        
        Args:
            range_step: Size of the age range (default: 1, e.g., 0-1, 1-2, etc.)
            
        Returns:
            dict: Dictionary with total children and list of ranges with quantities
            
        Example return:
            {
                "total_children": 25,
                "age_distribution": [
                    {"range": "0-1", "quantity": 5},
                    {"range": "1-2", "quantity": 8},
                    ...
                ]
            }
        """
        children = []
        self._inOrderTraversal(self._root, children)
        
        if not children:
            return {
                "total_children": 0,
                "age_distribution": []
            }
        
        # Sort children by age for consistent processing
        children_sorted = sorted(children, key=lambda x: x.age)
        max_age = max(child.age for child in children_sorted)
        
        # Initialize distribution and tracking
        distribution = []
        counted_children = set()
        
        # Create ranges from 0 to max_age + range_step to include the last range
        current_start = 0
        is_first_range = True
        
        while current_start <= max_age + range_step:
            range_end = current_start + range_step
            range_str = f"{current_start}-{range_end}"
            quantity = 0
            
            # Count children in current range that haven't been counted yet
            for child in children_sorted:
                if child.id not in counted_children:
                    # For first range: include start (>=), for others: exclude start (>)
                    # All ranges: include values up to and including range_end (<=)
                    if is_first_range:
                        if current_start <= child.age <= range_end:
                            quantity += 1
                            counted_children.add(child.id)
                    else:
                        if current_start < child.age <= range_end:
                            quantity += 1
                            counted_children.add(child.id)
            
            distribution.append({
                "range": range_str,
                "quantity": quantity
            })
            
            current_start = range_end
            is_first_range = False
        
        # Verify total count matches
        total_counted = sum(item["quantity"] for item in distribution)
        total_actual = len(children_sorted)
        
        # If there's a discrepancy, adjust the last non-zero range
        if total_counted != total_actual and distribution:
            # Find the last non-zero quantity range
            for i in range(len(distribution) - 1, -1, -1):
                if distribution[i]["quantity"] > 0:
                    distribution[i]["quantity"] += (total_actual - total_counted)
                    break
        
        # Remove empty ranges at the end (except if it's the only one)
        while len(distribution) > 1 and distribution[-1]["quantity"] == 0:
            distribution.pop()
        
        return {
            "total_children": total_actual,
            "age_distribution": distribution
        }
        
    def _deleteNode(self, node: Optional[TreeNode], childId: int) -> Optional[TreeNode]:
        """
{{ ... }}
        
        Args:
            node: Root of the subtree
            childId: ID of child to delete
            
        Returns:
            TreeNode: Root of the modified subtree
        """
        # Base case
        if node is None:
            return node
            
        # Recursive calls for ancestors of node to be deleted
        if childId < node.child.id:
            node.left = self._deleteNode(node.left, childId)
        elif childId > node.child.id:
            node.right = self._deleteNode(node.right, childId)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
                
            # Node with two children: get the inorder successor (smallest
            # in the right subtree)
            temp = self._minValueNode(node.right)
            
            # Copy the inorder successor's content to this node
            node.child = temp.child
            
            # Delete the inorder successor
            node.right = self._deleteNode(node.right, temp.child.id)
            
        return node
    
    def _minValueNode(self, node: TreeNode) -> TreeNode:
        """
        Find node with minimum value in BST (leftmost leaf)
        
        Args:
            node: Root of subtree
            
        Returns:
            TreeNode: Node with minimum value
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
