# ransom note (leetcode 383)

https://leetcode.com/problems/ransom-note/

> Given two stings `ransomNote` and `magazine`, return true if `ransomNote` can be constructed from `magazine` and false otherwise.

> Each letter in `magazine` can only be used once in `ransomNote`.

## solution

```
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for char in magazine:
            if char not in mag:
                mag[char] = 1
            else:
                mag[char] += 1
        
        for char in ransomNote:
            if char not in mag:
                return False
            if char in mag:
                mag[char] -= 1
        
        if all(x >= 0 for x in mag.values()):
            return True
        else:
            return False
```
