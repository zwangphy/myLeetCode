# reverse string (leetcode 344)

https://leetcode.com/problems/reverse-string/

> Write a function that reverses a string. The input string is given as an array of characters `s`.
> You must do this by modifying the input array in-place with O(1) extra memory.

## solution: two pointer

Reversing the array = Swapping `s[0]` with `s[-1]`, swapping `s[1]` with `s[-2]`, ...

```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1       
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

## solution 2: one-line solution

```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s.reverse()
```
