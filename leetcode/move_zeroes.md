# move zeroes (leetcode 283)

https://leetcode.com/problems/move-zeroes/

Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

## solution

Similar to the previous two questions. Use another pointer i to keep track the number of non-zero elements encountered. 
If `nums[j]` is non-zero, replace `nums[i]` by 'nums[j]'. Eventually, replace all the remaining elements by zero.

```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
```
