# Majority element (Leetcode 169)

https://leetcode.com/problems/majority-element/

> Given an array nums of size n, return the majority element. 
> The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

## Solution

```
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
            if count[nums[i]] > len(nums)/2:
                return nums[i] 
```  

If the majority element is not gaurenteed to be > n/2, complete the for loop and
```
return max(count,key=count.get)
```
