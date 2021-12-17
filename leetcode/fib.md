# Fibonacci numbers (leetcode 509)

https://leetcode.com/problems/fibonacci-number/

> The Fibonacci numbers, commonly denoted F(n) form a sequence, 
> called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
> starting from 0 and 1. That is,

> F(0) = 0, F(1) = 1
> F(n) = F(n - 1) + F(n - 2), for n > 1.

> Given n, calculate F(n).

## solution 1: dynamical programming

Append every Fib numbers to a list by adding previous two Fib numbers.
Time complexity: O(n), space complexity: O(n)

```
class Solution:
    def fib(self, n: int) -> int:
        
        fiblist = [0, 1]
        
        for i in range(2, n+1):
            fiblist.append(fiblist[i-1]+fiblist[i-2])
            
        return fiblist[n]
```

Alternately, we can initialize an array with all elements being zero. Then change the value in-place by the rule.

```
class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        fiblist = [0] * (n+1)
        fiblist[0], fiblist[1] = 0, 1
        
        for i in range(2, n+1):
            fiblist[i] = fiblist[i-1]+fiblist[i-2]
            
        return fiblist[n]
```

## solution 2: recursion

Recursion is very inefficient for computing Fib numbers. The time complexity is almost O(2^n).
See https://www.geeksforgeeks.org/time-complexity-recursive-fibonacci-program/

```
def fib(n):    
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```


## solution 3: iteration

time complexity: O(n), space complexity: O(1)

```
def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y
        return x
```

[//]: # (for _ in range. This link gives a nice intro to the underscore _ sign in python. https://www.datacamp.com/community/tutorials/role-underscore-python)  


## analytic formula

There is in fact an analytic formula to compute the n-th Fib number.

The floor function, floor(x), returns the greatest integer that is less than or equal to x. Then,

Fib(n) = floor(phi^n/sqrt(5) + 1/2), where phi = (1+sqrt(5))/2 = 1.618 is the goledn ratio number.

We can invert this formula to determine the greatest Fib number not exceeding a given integer.

# related problems

## climbing stairs (leetcode 70)

https://leetcode.com/problems/climbing-stairs/

> You are climbing a staircase. It takes n steps to reach the top.
> Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**solution**

This problem is almost identical to calculating Fib numbers. Suppose there are `f(n)` ways to climb a n-step stair. 
The final movement can either be a 1-step jump or a 2-step jump. Therefore,
```
f(n) = f(n-1) + f(n-2)
```
This recursive relation is exactly what produces Fib numbers.

## paving floor

> You are paving a rectangle floor of dimension 2 by n. The tiles you have are all 2 by 1 rectangles. 
> What's the number of distinct ways to pave the floor?

**solution**

The final pavement is either one tile vertically filled, or two tiles horizontally filled. So we have the recursion relation
```
f(n) = f(n-1) + f(n-2)
```
Rings a bell?

