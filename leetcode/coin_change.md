# coin change (leetcode 322)

https://leetcode.com/problems/coin-change/

> You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
> Return the fewest number of coins that you need to make up that amount. 
> If that amount of money cannot be made up by any combination of the coins, return -1.

> You may assume that you have an infinite number of each kind of coin.

## solution: dynamic programming

Let `dp[amount]` be the solution given `amount` and an array `coins`. 

If we pick our first coin to be `coins[i]`, the amount of money we need to make up is now reduced to `amount - coins[i]`. 
We can therefore express `dp[amount]` recursively via

```
dp[amount] = min(dp[amount - coins[i]]) + 1,
```
where the minimum is selected from `dp[amount - a[i]]` for all i. We can then deduce `dp[amount]` from `dp[1]`.

Codes:
```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        DP = [0] * (amount + 1)
        
        for a in range(1, amount + 1):
            temp = [DP[a - coin] for coin in coins if coin <= a and DP[a - coin] >= 0]
            if temp:
                DP[a] = 1 + min(temp)
            else:
                DP[a] = -1
            			        
        return DP[amount]
```
