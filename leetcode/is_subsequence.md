# is subsequence (leetcode 392)

https://leetcode.com/problems/is-subsequence/

Given two strings `s` and `t`, return true if `s` is a subsequence of `t`, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## solution 1: two pointer

### idea:
Similar to [remove element](/remove_element.md), let a pointer j be the index we loop the string `t` and another pointer i be the pointer to string 's'.
Initially, both i and j are set to zero. Then we check if `s[i]` appears in `t` by scanning `t[j]`. Update i only if `s[i] == t[j]`. Then check if
`s[i+1]` appears in the rest of `t`, and so forth. Return `True` if all `s[i]` is found, i.e. the final value of i equals `len(s)`.

Time complexity: O(n)

```
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if s and not t:
            return False
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
        return False 
```

## solution 2: dp

If `s[0]` is found in 't', reset `s = s[1:]` (namely, remove `s[0]`). Then check if `s[0]` in `t`. Repeat. 

```
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        for ch in t:
            if len(s) > 0 and ch == s[0]:
                s = s[1:]
        return len(s) == 0
```
