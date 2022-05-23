"""
Search a node in BST

Basic idea is to keep in mind  that in a BST left node is always smaller than the root element
and right is always greater than the root element

So if given value is smaller than the root node search on the left side , if it is greater it resides on the right side

"""

def search(root, k):

    if root ==None:
        return -1

    while root !=None:

        if root.data == k:
            #found
            return True

        if root.data<k:
            #resides on the right side of the root
            root = root.right

        if root.data>k:
            root = root.left
            #resides on the right side of the root

    return False #not found




