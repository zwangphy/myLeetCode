# jump game (leetcode 55)

https://leetcode.com/problems/jump-game/

> You are given an integer array `nums`. You are initially positioned at the array's first index, 
> and each element in the array represents your maximum jump length at that position.
> Return true if you can reach the last index, or false otherwise.

## solution 1: iterative

If we can reach the i-th index, the farthest index we can jump from there is `i+nums[i]`. 
Therefore, we can scan the array and keep the max value of `i+nums[i]`.

```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)-1):
            if farthest < i:
                break
            farthest = max(farthest, i+nums[i])
        return farthest >= len(nums)-1
```

## solution 2: dp
