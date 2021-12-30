# baseball game (leetcode 682)

https://leetcode.com/problems/baseball-game/

You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings `ops`, 
where `ops[i]` is the ith operation you must apply to the record and is one of the following:

1. An integer x - Record a new score of x.
2. "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
3. "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
4. "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.

Return the sum of all the scores on the record.

## solution

Append scores to a stack. Use `pop()` to remove the previous score when a "C" appears.

```
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2*stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
```

Alternate way to check if `op` is a  string of integer:
```
if op.isdigit() or op[0] == '-':
                stack.append(int(op))
```
