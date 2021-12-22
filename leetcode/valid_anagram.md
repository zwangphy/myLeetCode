# valid anagram (leetcode 242)

https://leetcode.com/problems/valid-anagram/

> Given two strings s and t, return true if t is an anagram of s, and false otherwise.

## solution

```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {letter: 0 for letter in s}
        for letter in s:
            dic[letter] += 1
        for letter in t:
            if letter not in s:
                return False
            else:
                dic[letter] -= 1
        return all(x == 0 for x in dic.values())
```
