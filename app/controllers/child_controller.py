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
    
    def deleteChild(self, childId: int) -> bool:
        """
        Delete child by ID
        
        Args:
            childId: ID of child to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        self._root = self._deleteNode(self._root, childId)
        return self._root is not None or self._root is not None
    
    def _deleteNode(self, node: Optional[TreeNode], childId: int) -> Optional[TreeNode]:
        """
        Delete node with given ID from BST
        
        Args:
            node: Current node
            childId: ID to delete
            
        Returns:
            TreeNode: Updated node
        """
        # Base case: empty tree
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
