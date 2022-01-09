# squares of a sorted array (leetcode 977)

https://leetcode.com/problems/squares-of-a-sorted-array/

> Given an integer array `nums` sorted in non-decreasing order, 
> return an array of the squares of each number sorted in non-decreasing order.

## solution 1: squaring each element and sorting

Time complexity: squaring takes O(n), sorting takes O(n logn)

```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
```

More compactly,

```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num*num for num in nums)
```

## solution 2: two pointer

The subtlety arises from the possibility that the input array may start with negative integers. 
That's why we need to sort the squared array.

Initialize an array of the same length as the output array to store the squared numbers.
As the first step, we can compare the leftmost number (which is the most "negative" number in the array) 
with the rightmost number (the most "positive"). If the absolute value of the leftmost is larger, 
after squaring it will become the largest number. So we store it at the rightmost entry of the output array. 
Next we compare the second leftmost to the rightmost, and so forth. 

Time complexity: O(n)

```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = [0] * (len(nums))
        left, right = 0, len(nums)-1
        for i in range(len(sq)-1, -1, -1):
            if abs(nums[left]) <= abs(nums[right]):
                sq[i] = nums[right]*nums[right]
                right -= 1
            elif abs(nums[left]) > abs(nums[right]): # must use elif not if
                sq[i] = nums[left]*nums[left]
                left += 1
        return sq
```
