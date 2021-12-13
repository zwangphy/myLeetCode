# Roman to Integer (leetcode 13)

https://leetcode.com/problems/roman-to-integer/

> Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. Given a roman numeral, convert it to an integer.

## solution

```
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        i = len(s)-1
        num = dic[s[i]]
        
        while i > 0:
            if dic[s[i-1]] >= dic[s[i]]:
                num += dic[s[i-1]]
            else:
                num -= dic[s[i-1]]
            i -= 1
        return num
```
