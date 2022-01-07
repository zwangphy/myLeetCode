# Min Cost Climbing Stairs (leetcode 746)

https://leetcode.com/problems/min-cost-climbing-stairs/

## solution: dp

Let `n = len(cost)`, we can initialize an array of length = n + 1. 
The (i+1)-th entry represents the min cost to reach the top of the i-th stair. Because the i-th stair must either be reached from the (i-1)-th or the (i-2)-th,
the recursion relation is then
`dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`. In this way we can derive the min total cost from bottom up.


```
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        dp = [0] * (n+1)        
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[-1]
``` 
