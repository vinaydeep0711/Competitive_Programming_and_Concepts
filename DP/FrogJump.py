"""There is a frog on the 1st step of an N stairs long staircase. The frog wants to reach the Nth stair. HEIGHT[i] is the height of the (i+1)th stair.If Frog jumps from ith to jth stair, the energy lost in the jump is given by |HEIGHT[i-1] - HEIGHT[j-1] |.In the Frog is on ith staircase, he can jump either to (i+1)th stair or to (i+2)th stair. Your task is to find the minimum total energy used by the frog to reach from 1st stair to Nth stair."""
"""
10 20 30 10

out - 20
"""
import sys
sys.setrecursionlimit(10**6)

#recursion
def frog_jump(heights,n):

    if n==0:
        return 0

    left = frog_jump(heights,n-1)+abs(heights[n]-heights[n-1])
    right = float('inf')
    if n>1:
        right = frog_jump(heights, n-2)+abs(heights[n]-heights[n-2])

    return min(left,right)

print(frog_jump([10, 20, 30, 10],3))



#convert recursion to dp
def frog(heights, n, dp):
	if n==0:
		return 0
	if dp[n] !=-1:
		return dp[n]
	left = frog(heights,n-1, dp)+abs(heights[n-1]- heights[n])
	right = float('inf')
	if n >1:
		right = frog(heights,n-2, dp)+abs(heights[n-2]-heights[n])

	dp[n]=min(left, right)
	return dp[n]

ind=3
dp = [-1 for i in range(0, ind+1)]
print(frog([10, 20, 30, 10],ind,dp))



#final dp solution

def frog_jump2(heights, n):
    dp = [0 for _ in range(0,n)]
    dp[0]=0 #since in the recursion last indeex =0
    for i in range(1,n):
        left = dp[i-1]+abs(heights[i-1]-heights[i])
        right=float('inf')
        if i>1:
            right = dp[i-2]+abs(heights[i-2]-heights[i])
        dp[i]=min(left,right)
    return dp[-1]

print(frog_jump2([10, 20, 30, 10],4))
