# valid palindrome (leetcode 125)

https://leetcode.com/problems/valid-palindrome/

> A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
> Alphanumeric characters include letters and numbers.

> Given a string s, return true if it is a palindrome, or false otherwise.

## solution

```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True
```

Alternately, we can create a reverse string by `s2 = s[::-1]`, and then `return s == s2`.
