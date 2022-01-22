# minimum path sum (leetcode 64)

https://leetcode.com/problems/minimum-path-sum/

## solution: dp

Let `dp[i][j]` be the min path sum to `grid[i][j]`. Some special cases:
* if `i = j = 0`, then `dp[i][j] = grid[i][j]`
* if `i = 0` and `j > 0`, you can only go straight along this row, so `dp[i][j] = dp[i][j-1] + grid[i][j]`
* likewise for `j = 0` and `i > 0`

For other values of i and j, we can reach `grid[i][j]` either from `grid[i-1][j]` or `grid[i][j-1]`. Therefore,

`dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i-1][j] + grid[i][j])`.

```
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp =[ [0]*n ]* m
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
```
