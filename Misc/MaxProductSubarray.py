"""Find Max Product Subarray
   example1= 6, -3, -10, 0, 2
   MaxSubarrayProduct = 180
   example2 = -8 5 3 16
   MaxSubarrayProduct = 90
"""

""" idea is to find maxProduct by multiplying each array values and get the max product but if we encounter 0 at nay place 
    then if will multiply with 0 all further product values will become 0 so instead will keep the the product vale as 1 so the when 
    we will multiply further it will produce subarray product.
    
    in example two -8 is at start and we dont have any other negative number So if we calculate product result will be always in negative 
    to fix that we can calculate product from left as well as right side and find the max.
"""


def MaxProductSubArray(arr):
    maxProdLeft= float('-inf')
    prod = 1
    for i in range(0, len(arr)):
        if arr[i]==0:
            prod=1
            continue
        prod = prod*arr[i]
        maxProdLeft = max(maxProdLeft,prod)

    maxProdRight = float('-inf')
    prod=1
    for i in range(len(arr)-1, -1,-1):
        if arr[i]==0:
            prod=1
            continue
        prod = prod*arr[i]
        maxProdRight = max(maxProdRight,prod)

    return max(maxProdRight, maxProdLeft)


print(MaxProductSubArray([6, -3, -10, 0, 2]))
print(MaxProductSubArray([-8, 5, 3, 1, 6]))
