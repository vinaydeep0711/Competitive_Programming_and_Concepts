"""Check if BBST"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root) -> bool:

        if root == None:
            return True

        if abs(self.height(root.left) - self.height(root.right)) < 2 \
                and self.isBalanced(root.left) \
                and self.isBalanced(root.right):
            return True
        return False

    def height(self, root):

        if root == None:
            return -1

        left = self.height(root.left) + 1
        right = self.height(root.right) + 1

        return max(left, right)





