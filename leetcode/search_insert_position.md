# Search insert position (leetcode 35)

https://leetcode.com/problems/search-insert-position/

> Given a sorted array of distinct integers and a target value, return the index if the target is found. 
> If not, return the index where it would be if it were inserted in order.
>
> You must write an algorithm with O(log n) runtime complexity.

## binary search

First, check if target < nums[0] or target >= nums[-1].

Then repeat the binary search procedure until (1) nums[mid] = target, return mid, or (2) high - low = 1, return low if nums[low] = target, else return high.

```
class Solution(object):
    def searchInsert(self, nums, target):
        
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums)-1
        if target > nums[-1]:
            return len(nums)
        
        low = 0
        high = len(nums)
        mid = (low+high)//2
        
        while high - low > 1:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid
                mid = (low+high)//2
            if nums[mid] > target:
                high = mid
                mid = (low+high)//2
                
        return low if nums[low] == target else high
```
