# Valid parentheses (Leetcode 20)
https://leetcode.com/problems/valid-parentheses/
> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

## Standard solution with stack

*Basic idea*: Starting from the first element, if it is a left parenthesis, store it to a stack. When you see a right parenthesis, check if it matches with the last element of the stack. Not match: return false; matches: pop the stack and go forward.

*Some corner cases*: 

1. {})( is not valid. The stack becomes empty when } matches with {. Therefore, when you see a right parenthesis, you need to check if the stack is empty.
2. ((((((((( is not valid. If a sequence is valid, the stack must be empty in the end.


```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        N = len(s)
        valid_parenthese = {'(': ')', '{': '}', '[': ']'}
    
        if N % 2 != 0:
            return False
    
        for i in range(N):
            if s[i] in valid_parenthese.keys():
                stack.append(s[i])
            else:
                if stack:
                    if valid_parenthese[stack.pop()] != s[i]:
                        return False
                else:
                    return False
    
        if not stack:
            return True
        else:
            return False
```

More compact code
```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_parenthese = {'(':')', '{':'}','[':']'}
        for c in s:
            if c in p:
                stack.append(valid_parenthese[c])
            elif c in p.values():
                if stack == [] or c != stack.pop():
                    return False
        return not stack
```

## Neat solution

Replace any (), [], {} by white space. In the end, a valid sequence will be totally erased empty.

```
class Solution(object):
    def isValid(self, s):
         while True:
            if '()' in s:
                s = s.replace("()","")
            elif '{}' in s:
                s = s.replace ("{}","")
            elif '[]' in s:
                s = s.replace("[]","")
            else:
                return not s
```            
