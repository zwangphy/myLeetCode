# arithmetic slices (leetcode 413)

https://leetcode.com/problems/arithmetic-slices/

## solution: sliding window

This question is similar to the previous question substrings of identical characters.

Let the first sliding window start from index `l = 1`. We scan the input array from index `i = 2`.
If `nums[i] - nums[i-1] = nums[l] - nums[l-1]`, continue. Otherwise, reset the the sliding window to start from `i`.

In an arithmetic arrays of length y, there are 1 subarray of length y, 2 of length y-1, ..., y-1 of length 2 and y of length 1.
In total, there are y*(y+1)/2 subarrays. All the subarrays with at least three elements are also arithmetic. So the number of
arithmetic slices is y*(y+1)/2-2y+1.

Note: don't forget to count in the arithmetic slices in the final sliding window.

Complexity: time O(n), space O(1)

```
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        elif n == 3:
            return 0 if nums[1]-nums[0] != nums[2]-nums[1] else 1
        else:
            
            res = 0
            
            i = 2
            l = 1
            
            while i <= n - 1:
                y = i - l + 1
                if nums[i]-nums[i-1] != nums[l]-nums[l-1]:
                    res += y*(y+1)/2 - 2*y +1
                    l = i
                    i = l+1
                else:
                    i += 1
            y = i - l + 1
            return int(res+y*(y+1)/2 - 2*y +1)
                    
                    
                    
                    
        
```
