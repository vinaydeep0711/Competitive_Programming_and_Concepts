"""Given Inorder and preorder construct a Binary Tree"""


## Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    def buildTree(self, A, B):
        dic =dict()
        for i in range(0,len(B)):
                dic[B[i]]=i
        return self.inPreOrder(0,len(A)-1, 0, len(B)-1,dic, A,B)


    def inPreOrder(self,ps, pe,ins,inse,dic,A,B):

        if ps>pe:
            return None
        root = TreeNode(A[ps])
        inindx = dic[A[ps]]
        Nodesinleft = inindx-ins


        root.left = self.inPreOrder(ps+1,ps+Nodesinleft, ins, inindx-1,dic,A,B)
        root.right =self.inPreOrder(ps+Nodesinleft+1,pe, inindx+1, inse,dic,A,B)
        return root





