# find the difference (leetcode 389)

https://leetcode.com/problems/find-the-difference/

You are given two strings `s` and `t`.

String `t` is generated by random shuffling string `s` and then add one more letter at a random position.

Return the letter that was added to `t`.

## solution

```
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for char in t:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        for char in s:
            dic[char] -= 1
            
        for key, value in dic.items():
            if value == 1:
                return key
```
