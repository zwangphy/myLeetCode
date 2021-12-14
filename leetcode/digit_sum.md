# Digit sum

Given a positive integer n, return the sum of its digit number. 
For example, if n = 12, return 3 (because 1 + 2 = 3).

## solution

```
def digitSum(n):
    res = 0
    while n >= 1:  
        a = n%10
        res += a
        n = n//10
    return res        
```
