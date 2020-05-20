# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:19:18 2020

@author: Sri
"""
404. Sum of Left Leaves


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def check_leaf(element):
            return element is not None and element.left is None and element.right is None
    
        final_list = []
        queue = [root]
        while queue:
            element = queue.pop(0)
            if check_leaf(element.left):
                final_list.append(element.left.val)
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
        return sum(final_list)