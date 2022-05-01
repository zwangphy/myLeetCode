# Backspace String Compare (leetcode 844)

https://leetcode.com/problems/backspace-string-compare/

## solution 1: stack

Use a stack to store the backspace string. Time O(n), space O(n). 
Caution: make sure that backspacing an empty string results in an empty string (but you can't apply `pop()` on an empty stack).

```
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def bp(st):
            stack = []
            for char in st:
                if char == '#':
                    if stack:
                        stack.pop()
                        continue
                    if not stack:
                        continue
                else:
                    stack.append(char)
            return stack
        return bp(s) == bp(t)
```

## solution 2

