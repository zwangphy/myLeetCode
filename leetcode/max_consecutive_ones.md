# max consecutive ones (leetcode 485)

https://leetcode.com/problems/max-consecutive-ones/

Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array.

# solution

For every block of consecutive one's, set up a window. Record the length.

Time complexity: O(n)

Alternately, we can use a variable `consecutive_ones` to store the number of consecutive ones. 
Starting from the first one in a block, add `consecutive_ones` by 1 for every one in the block. 
If `nums[i] = 0`, reset `consecutive_ones` to zero.

```
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_ones = 0
        max_consecutive = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                consecutive_ones += 1
                max_consecutive = max(consecutive_ones, max_consecutive)
            if nums[i] == 0:
                consecutive_ones = 0
        return max_consecutive
```

