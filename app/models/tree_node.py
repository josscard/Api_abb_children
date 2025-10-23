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
