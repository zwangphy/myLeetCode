# first unique character in a string (leetcode 387)

https://leetcode.com/problems/first-unique-character-in-a-string/

> Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

## solution

```
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                dic[s[i]] = -1
        
        for key, value in dic.items():
            if value != -1:
                return value
        return -1
```

# related question: first repeating character in a string

> Given a string `s`, find the first repeating character in it and return this character. If it does not exist, return `-1`.

## solution

```
class Solution:
    def firstChar(self, s: str) -> int:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                return char
        return -1
```
