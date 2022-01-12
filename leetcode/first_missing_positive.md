# first missing positive (leetcode 41)

https://leetcode.com/problems/first-missing-positive/

## naive solutions: 

1. Brute force searching: starting from `i = 1`, search if `i` is in the array; `i += 1`. 
Searching an element in an arary takes O(n) time, and in the worst case we need to search n+1 numbers. So time complexity O(n^2).
2. Sort the array and then search. Time complexity O(log n).
3. Store the numbers in the array to a dictionary or a set. Since searching in a dictionary takes O(1) time, we have reduced the overall
time complexity to O(n). But this algo requires O(n) space. A small trick to slightly reduce space complexity is noting that we only need to
store positive numbers smaller than the length of the array. If there is a number larger than the length of the array, the first missing positive
must be smaller than the array's length.

Codes for the third algo:

```
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        s = {x for x in nums if x > 0 or x <= len(nums)}
               
        for i in range(len(nums)+1):
            if i+1 not in s:
                return i+1
```

## solution 2: O(n) time + O(1) space

First let's sort all the non-positive numbers to the left and all the positive ones to the right. 
Consult [sort array by parity](/leetcode/sort_array_by_parity.md) to see how to achieve it by a two-pointer algo.

