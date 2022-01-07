# Remove element (Leetcode 27)

https://leetcode.com/problems/remove-element/

> Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in nums in-place. The relative order of the elements may be changed.

## Solution

**Basic idea**:

Loop through every element in the list with index j. Create another index i, which tracks the nuumber of elements not equal to `val`. 
If the `nums[j] != val`, add i by one and update nums[i] by nums[j].

```
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
``` 
