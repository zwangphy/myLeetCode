# maximum subarray (leetcode 53)

https://leetcode.com/problems/maximum-subarray/submissions/

## solution 1: brute force

Compute the sum of all subarrays and select the max value. Time complexity: O(n^2)

```
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        
        sum_from_i, sum_max = nums[0], nums[0]
        if n == 1:
            return sum_max
        
        for i in range(n):
            sum_from_i = nums[i]
            sum_max = max(sum_max, sum_from_i)
            for j in range(i+1, n):
                sum_from_i +=  nums[j]
                sum_max = max(sum_max, sum_from_i)
        return sum_max
```

## solution 2: dp

Consider the max subarray among all subarrays ending at i-th index, let the max sum be `dp[i]`. Then 
```
dp[i+1] = max(dp[i] + nums[i+1], nums[i+1]).
```
That is, the max subarray ending at (i+1)-th must either be the pervious subarray augmented by `nums[i+1]`, or `nums[i+1]` itself.

With this recursion relation, for every index in the input array, we can find the max subarray ending at that index. Return the max.

Time complexity: O(n)

```
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * (n)
        
        dp[0] = nums[0]
        
        for i in range(1,n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
```

## solution 3: divide and conquer

O(n)

## solution 4: Kadane algorithm

Initialize two variables `maxSum = nums[0]` and `currSum = 0`. Loop i. 
Compute the sum accumulated thus far, and store its value to `currSum`. 

If `currSum` is negative, we update `currSum = 0`. This is because, instead of adding the next element in the array to a negative sum, we better
restart the sum from the next element. 

```
class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        currSum = 0
        
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(currSum, maxSum)
        
        return maxSum
```
