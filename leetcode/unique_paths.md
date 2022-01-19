# unique paths (leetcode 62)

https://leetcode.com/problems/unique-paths/

## solution: dp

Let `dp[i][j]` be the number of unique paths to `grid[i][j]`. 
Along the top row and the first column, `dp[0][i] = 1` and `dp[0][j] = 1`. 

To arrive at other `grid[i][j]`, there are two options: from the grid point above it or to the left of it. 
So `dp[i][j] = dp[i-1][j] + dp[i][j-1]`

```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n)] * (m)
        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
```

## solution 2: analytic solution

If the dimension of the grid is m x n, the total steps needed to arrive at the lower right corner is m + n.
You can assign the m steps going down and the n steps going right in m + n slots. 
So the number of ways is choosing m from m + n (or equivalently, choosing n from m + n).
