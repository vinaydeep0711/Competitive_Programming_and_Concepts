"""You are given an array/list of ‘N’ integers.
You are supposed to return the maximum sum of the subsequence with the
constraint that no two elements are adjacent in the given array/list."""

from sys import stdin




def maximumNonAdjacentSum(nums):
    dp = [-1 for _ in range(0, len(nums))]
    return f(len(nums) - 1, nums, dp)


# recursion
# def f(ind, num):
#     if ind==0: return num[ind]
#     if ind<0: return 0
#     pick = num[ind]+ f(ind-2,num)
#     notpick = 0+f(ind-1,num)
#     return max(pick,notpick)

# dp +recur
def f(ind, num, dp):
    if ind == 0: return num[ind]
    if ind < 0: return 0
    if dp[ind] != -1: return dp[ind]
    pick = num[ind] + f(ind - 2, num, dp)
    notpick = 0 + f(ind - 1, num, dp)
    dp[ind] = max(pick, notpick)
    return dp[ind]

#dp
def maximumNonAdjacentSum2(nums):
    dp = [0 for _ in range(0,len(nums))]
    dp[0]=nums[0]
    neg =0
    for i in range(1, len(nums)):
        pick = nums[i]
        if i>1:
            pick +=dp[i-2]
        notpick = 0+dp[i-1]
        dp[i]=max(pick, notpick)
    return dp[-1]


# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    print(maximumNonAdjacentSum2(arr))

    t -= 1