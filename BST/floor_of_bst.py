"""
Given  K find floor of BST

when we say find floor means we want to find value wick is just smaller than k in the tree
"""


class Solution:
    # @param A : root node of tree
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        finalans = []
        for i in range(0, len(B)):
            lis = []
            floor = self.floor(A, B[i])
            ciel = self.ciel(A, B[i])
            lis.append(floor)
            lis.append(ciel)
            finalans.append(lis)
        return finalans

    def floor(self, A, k):
        ans = -1
        while A != None:
            if A.val == k: return k
            if A.val > k:
                A = A.left
            else:
                ans = A.val
                A = A.right
        return ans

    def ciel(self, A, k):
        ans = -1
        while A != None:

            if A.val == k: return k
            if A.val > k:
                ans = A.val
                A = A.left
            else:
                A = A.right
        return ans   

