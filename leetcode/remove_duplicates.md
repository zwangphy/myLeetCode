# remove duplicates from sorted array (leetcode 26)

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## solution

Similar to the previous problem

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        L = len(nums)
        
        j = 1
        
        for i in range(1,L):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
```
