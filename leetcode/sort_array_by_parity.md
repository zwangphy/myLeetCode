# sort array by parity (leetcode 905)

https://leetcode.com/problems/sort-array-by-parity/

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

## solution

Similar to the previous question. Loop the array by two pointer, i from left and j from right.

If `nums[i]` is even, we keep its position and reset `i += 1`. Likewise for odd `nums[j]`. 
When `nums[i]` is odd and `nums[j` is even simultaneously, swap their positions.
(Note that you must make sure that if `nums[i]` and `nums[j] `are both odd or both even,
only one of the pointers gets updated and the other stays there.)

Time complexity: O(n)

```
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i]%2 == 0:
                i += 1
            if nums[j]%2 == 1:
                j -= 1
            elif nums[i]%2 == 1 and nums[j]%2 == 0: # must use elif here; not if
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums
```
