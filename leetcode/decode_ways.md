# Decode ways (leetcode 91)

https://leetcode.com/problems/decode-ways/

### solution: dynamical programming

Consider a string of length n, and denote the number of decode ways by `dp(n)`. BecauseIn general, there are two classes of decoding ways. 

* Class 1: if the final letter is nonzero, we can first decode the first n-1 numbers in the string, and then decode the final letter. If the final letter is 0, because 0 itself is an invalid sequence to decode and therefore the number of decode ways from this strategy is zero.
* Class 2: if the final 2 letters form a number between 10 and 26, we can first decode the first n-2 numbers, and decode the final 2 numbers to a single letter.

Mathematically, we find a recursive relation

``` math
dp(n) = dp1(n-1) + dp2(n-2),
```
where
```math
dp1(n-1) = dp(n-1) if the n-th number is nonzero, and dp1(n-1) = 0 if the n-th number is zero.
dp2(n-2) = dp(n-2) if the number formed by the last two numbers is between 10 and 26, and dp2(n-2) = 0 otherwise.
```

**Code**:
```
class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n)
        
        if s[0] == '0':
            dp[0] = 0
        else:
            dp[0] = 1
        
        for i in range(1,n):
            if i == 1:
                dp1 = (0 if s[i] == '0' else dp[i-1])
                dp2 = (1 if 10 <= int(s[i-1:i+1]) <= 26 else 0)
                dp[i] = (dp1) + (dp2)
            else:
                dp1 = (0 if s[i] == '0' else dp[i-1])
                dp2 = (dp[i-2] if 10 <= int(s[i-1:i+1]) <= 26 else 0)
                dp[i] = (dp1) + (dp2)
        
        return dp[n-1]
```        
