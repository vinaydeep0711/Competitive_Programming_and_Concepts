"""
Idea is tto find a place where k can fit in
since its BST wee need to search a place where lst is smaller than k and rst is greater than the k
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val: int):
        if root == None:
            return TreeNode(val)

        temp = root
        parent = None

        while temp:
            parent = temp

            if val >= temp.val:
                # goto right
                temp = temp.right
            elif val < temp.val:
                # goto left
                temp = temp.left

        #now we have found parent of the position where we want to insert our new node
        #we can now cheeck if we need to insert at left or right
        if val >= parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root





