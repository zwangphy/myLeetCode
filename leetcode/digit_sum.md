# Digit sum

Given a positive integer n, return the sum of its digit number. 
For example, if n = 12, return 3 (because 1 + 2 = 3).

## solution

Let's say n = 123. To get the last digit, 3, we can calculate `n%10`. To get the second digit, 2, we calculate `n%100`, and so forth.
Iteratively, after calculating `n%10` we can reset `n = n//10` and repeat the process.

```
def digitSum(n):
    res = 0
    while n >= 1:  
        a = n%10
        res += a
        n = n//10
    return res        
```
