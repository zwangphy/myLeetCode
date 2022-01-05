# array partition 1 (leetcode 561)

https://leetcode.com/problems/array-partition-i/

> Given an integer array nums of 2n integers, group these integers into n pairs `(a1, b1), (a2, b2), ..., (an, bn)` 
> such that the sum of `min(ai, bi)` for all i is maximized. Return the maximized sum.

## solution

Sort the array. The max sum will be the sum of `nums[0] + nums[2] + ... + nums[2n-1]`.

```
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxsum = 0
        for i in range(0, len(nums), 2):
            maxsum += nums[i]
        return maxsum
```        
