# Fibonacci numbers (leetcode 509)

https://leetcode.com/problems/fibonacci-number/

> The Fibonacci numbers, commonly denoted F(n) form a sequence, 
> called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
> starting from 0 and 1. That is,

> F(0) = 0, F(1) = 1
> F(n) = F(n - 1) + F(n - 2), for n > 1.

> Given n, calculate F(n).

## Append first n Fib numbers to a list

```
class Solution:
    def fib(self, n: int) -> int:
        
        fiblist = [0, 1]
        
        for i in range(2, n+1):
            fiblist.append(fiblist[i-1]+fiblist[i-2])
            
        return fiblist[n]
```

## Recursion

```
def fib(n):    
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

Recursion is very inefficient for computing Fib numbers. The time complexity is almost O(2^n).
https://www.geeksforgeeks.org/time-complexity-recursive-fibonacci-program/


## Dynamical programming

```
def fib(self, n: int) -> int:
        x,y=0,1
        for _ in range(n):
            x,y=y,x+y
        return x
```

This link gives a nice intro to the underscore _ sign in python.
https://www.datacamp.com/community/tutorials/role-underscore-python

## Analytic formula

There is in fact an analytic formula to compute the n-th Fib number.

The floor function, floor(x), returns the greatest integer that is less than or equal to x. Then,

Fib(n) = floor(phi^n/sqrt(5) + 1/2), where phi = (1+sqrt(5))/2 = 1.618 is the goledn ratio number.

We can invert this formula to determine the greatest Fib number not exceeding a given integer.
