# valid mountain array (leetcode 941)

https://leetcode.com/problems/valid-mountain-array/

## solution: two pointer

First of all, a valid mountain array has at least three numbers.

Secondly, if the second number <= the first number, or the last number >= the second last number, it's not a valid mountain array.

For more general cases, we can use two pointers, one from left and the other from right. 
For the left pointer, i, if and only if `arr[i+1] > arr[i]`, we increment i by one. Otherwise, i stops there.
Similar for j. If and only if `arr[j-1] > arr[j]`, we update j by j-1.

Eventually, i and j will be equal in a valid mountain array.

Time complexity: O(n)

```
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i, j = 0, n-1
        if n < 3 or arr[i+1] <= arr[i] or arr[j-1] <= arr[j]:
            return False
        while arr[i+1] > arr[i]:
            i += 1
        while arr[j-1] > arr[j]:
            j -= 1
        return i == j
```
