# arithmetic slices (leetcode 413)

https://leetcode.com/problems/arithmetic-slices/

## solution: sliding window

This question is similar to the previous question substrings of identical characters.

Let the first sliding window start from index `l = 1`. We scan the input array from index `i = 2`.
If `nums[i] - nums[i-1] = nums[l] - nums[l-1]`, continue. Otherwise, reset the the sliding window to start from `i`.

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
