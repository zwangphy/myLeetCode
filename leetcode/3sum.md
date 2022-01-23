# 3 sum (leetcode 15)

https://leetcode.com/problems/3sum/

## solution: 2 sum + two pointer

We can covert 3 sum to a 2 sum problem in the following way. 
For every element `nums[i]` in the input array, we want to find two elements in `nums[i+1:]` that sum to `-nums[i]`.
Namely, we have a 2 sum problem for every subarray `nums[i+1:]` for i >= 1.

In [2 sum](/leetcode/two_sum.md), we introduced a number of methods. The optimal solution here would be 2 pointer.

The complication is the need to avoid duplicates. There are two types of duplicates.
* If `nums[i+1] = nums[i]`, we skip `nums[i+1]`.
* For a particular `nums[i]`, suppose we already find `nums[j] + nums[k] = -nums[i]`.
* If `nums[j+1] = nums[j]` or `nums[k-1] = nums[k]`, we skip them.

```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        if len(nums) <= 1:
            return res
        
        nums.sort()
        
        if nums[0] > 0 or nums[-1] < 0:
            return res
        
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            x = -nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == x:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while left <= len(nums) - 1 and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] > x:
                    right -= 1
                else:
                    left += 1
        if res:
            return res
```
