# house robber I (leetcode 198)

https://leetcode.com/problems/house-robber/

## solution: dp

Let `dp[n]` be the max amount up to (n+1)-th house,

```
dp[n] = max(dp[n-1], dp[n-2] + nums[n])
```

(If `nums = [3,1,1,3]`, the solution would be `3 + 3 = 6`. Why is there not a term of `dp[n-3] + nums[n]` in the recursion?
Because when we compute `dp[n-2]`, we've already taken the max between `dp[n-3]` and `dp[n-4] + nums[n-2]`.)

```
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
    
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(dp[i-1], nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
                
        return dp[-1]
```

Alternately, we can define `dp[n]` to be the max amount with the (n+1)-th house to be the last house robbed.
In the end, return `max(dp[-1], dp[-2])`.

# house robber II
