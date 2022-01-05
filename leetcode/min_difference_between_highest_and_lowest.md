# Minimum Difference Between Highest and Lowest of K Scores (leetcode 1984)

https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

# solution

Sort the array. The minimum difference will be one of `nums[k-1] - nums[0]`, `nums[k] - nums[1]`, ...

```
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        diff = nums[k-1] - nums[0]
        while i+k-1 < len(nums):
            diff = min(diff, nums[i+k-1] - nums[i])
            i += 1
        return diff
```

More compactly,
```
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i+k-1] - nums[i] for i in range(len(nums)-k+1))
```
