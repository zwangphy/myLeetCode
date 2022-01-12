# sort colors (leetcode 75)

https://leetcode.com/problems/sort-colors/

> Given an array `nums` with n objects colored red, white, or blue, 
> sort them in-place so that objects of the same color are adjacent, 
> with the colors in the order red, white, and blue.
>
> We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
>
> You must solve this problem without using the library's sort function.

## solution 1: three pointers

Let's first think about how to sort all the twos to the end of the array. Let `k = len(nums) -1` be the end index of the array. 
Loop the array. Every time we see a two, swap it with `nums[k]` and reset `k -= 1`. Eventually all the twos will be rearranged to the right
side of the array.

Now let's think about how to sort zeros and ones at the same time. Let i and j track the number of zeros and the sum of zeros and ones seen by far.
The expected outcome is that all the zeros sit on the first i indices and all the ones are between i and j.

If we see a one, increment only j by 1. If we see a zero, swap it with `nums[j]` and increment both i and j by 1. The procedure stops when j = k.

Complexity: time O(n), space O(1)

```
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[j] == 1:
                j += 1
            elif nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
```

## solution 2: two pass

Scan the array, record the number of zeros, ones and twos respectively, say = i, j, k.

Loop the array again, for the first i elements, rewrite them by zero; 
for the element between i and j, rewrite them by one; 
rewrite the rest by two.

```
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for color in nums:
            if color == 0:
                red += 1
            if color == 1:
                white += 1
            if color == 2:
                blue += 1
        
        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < red + white:
                nums[i] = 1
            else:
                nums[i] = 2
```
