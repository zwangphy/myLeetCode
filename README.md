# myLeetCode
my solutions to some leetcode and other coding problems

## Number of good subsets
https://leetcode.com/discuss/interview-question/268604/Google-interview-Number-of-subsets
> For a given list of integers and integer K, find the number of non-empty subsets S such that min(S) + max(S) <= K.

**Solution 1:**

Sort the list:

a[1], a[2], ..., a[i], a[i+1], ..., a[j],...

For every pair of i and j >= i, check if a[i] + a[j] <= K. If yes, then {a[i], a[j]} + any subset (including empty subset) formed by numbers between i and j is a good subset. There are j-i-1 numbers between i and j (for j >= i + 1), so the number of subset formed by these numbers is 2^(j-i-1).


```
def goodSubset(a, K):
    nums = 0    
    a.sort()    
    for i in range(len(a)):    
        for j in range(i,len(a)):
            if a[i] + a[j] <= K:
                if j <= i + 1:
                    nums += 1
                if j >= i + 2:
                    nums += 2**(j-i-1)
    return nums
 ```

Overall complexity: O(n^2)

**Better solution**

Sort the list. For i, use binary search to find the max j such that a[i] + a[j] <= K.

```
```

Overall complexity: O(n logn)

## Valid parentheses (Leetcode 20)
https://leetcode.com/problems/valid-parentheses/
> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

**Standard solution with stack**

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

**Neat solution**

For any (), [], {} in the list, replace it by white space. In the end, a valid sequence will be totally erased.

```
class Solution(object):
    def isValid(self, s):
        for i in range(int(len(s)/2)):
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
			if len(s) == 0:
				return True
        if len(s) != 0:
            return False
```            
