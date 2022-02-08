# best time to buy and sell stock I (leetcode 121)

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## solution: dp

Initialize a variable `min_ = prices[0]` and `max_profit = 0`. Scan the input array. 
The former variable will store the min price, i.e. update the value of `min_` if the current price is smaller than `min_`.
The latter will store the max profit, which needs to be updated if `current price - min_ > max_profit`. 

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        max_profit = 0
        for p in prices:
            min_ = min(p, min_)            
            max_profit = max(p - min_, max_profit)

        return max_profit
```

