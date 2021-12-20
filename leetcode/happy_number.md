# happy number (leetcode 202)

https://leetcode.com/problems/happy-number/

> Write an algorithm to determine if a number n is happy.

> A happy number is a number defined by the following process:

> Starting with any positive integer, replace the number by the sum of the squares of its digits.
> Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
> Those numbers for which this process ends in 1 are happy.
> Return true if n is a happy number, and false if not.

## solution

First of all, we write a helper function to transform the number in the prescribed way. This is similar to the previous problem [digit sum](/digit_sum.md). 
We can then use a set to store the result, until either 1 (return true) or a repeating result (return false) is obtained.

```
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sq(N):
            sq = 0
            while N >= 1:
                sq += (N%10) * (N%10)
                N //= 10
            return sq
        
        s = set()
        while n not in s:
            s.add(n)
            n = get_sq(n)
        return n == 1
```
