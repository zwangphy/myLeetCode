# Generate parentheses (leetcode 22)

https://leetcode.com/problems/generate-parentheses/

> Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## brute force 

Generate all permuatations and select the valid ones.

Complexity: O(n 2^(2n))

## backtracking

Keep track of how many ('s and )'s we have placed, say n_left and n_right. 
If n_left <= n, we can add one more ( to the end; if n_right < n_left, we can add one ) to the end.

```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
```

Complexity: ?
