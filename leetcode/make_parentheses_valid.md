# minimum add to make parentheses valid (leetcode 921)

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

## solution

Idea is similar to the previous question. We append parentheses in the input string one by one  to a stack, with one exception:

If the current parenthesis is a ')' and the last element of the stack is a '(', we pop '(' and do not append ')'.

In the end, the stack contains all invalid parentheses (if any), so the min add is equal to the length of the stack.

```
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        for char in s:
            if stack and stack[-1] == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack)
```

Note: the condition `if stack` is neccessary so as to ensure `stack[-1]` exists.
