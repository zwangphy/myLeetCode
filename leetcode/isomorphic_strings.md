# isomorphic strings (leetcode 205)

https://leetcode.com/problems/isomorphic-strings/

> Given two strings s and t, determine if they are isomorphic.

> Two strings s and t are isomorphic if the characters in s can be replaced to get t.

> All occurrences of a character must be replaced with another character while preserving the order of characters. 
> No two characters may map to the same character, but a character may map to itself.


## solution: hash table

If `s` and `t` are isomorphic, their characters have a one-to-one correspondance 
and this correspondance can be stored in a dictionary such that `dic[s[i]] = t[i]`. 
For these situations we need to return false:
1. If `len(s) != len(t)`, return false.
2. If `s[i]` is not `dic` but `t[i]` is already in `dic.values()`, return false because no two characters may map to the same character.
3. If `s[i]` is already in `dic` but `dic[s[i]] != t[i]`, return false because `s[i]` can't map to two characters.

Time complexity: O(n), space: O(n)

```
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
            elif dic[s[i]] != t[i]:
                return False
        return True
```
