"""Given the root of a binary tree, determine if it is a valid binary search tree (BST)."""

""" 
Idea1 - 
Check if inorder of BST is sorted if it is sorted it is a valid BST 
"""

"""
idea2-

check if root node is always greater then then max of LST and min of RST if yes its BST
"""

"""
idea 4 - we have to check if node are in range
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    def isValidBST(self, root) -> bool:
        # setting left range as -infinity and right range as +infinity
        return self.isBst(root, float('-inf'), float('inf'))

    def isBst(self, root, left, right):
        if root == None:
            return True  # we reached till last node so return True

        if root.val >= left and root.val <= right:
            return self.isBst(root.left, left, root.val - 1) and self.isBst(root.right, root.val + 1, right)
        return False