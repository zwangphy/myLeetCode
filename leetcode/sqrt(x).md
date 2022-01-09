# sqrt(x) (leetcode 69)

https://leetcode.com/problems/sqrtx/

> Given a non-negative integer x, compute and return the square root of x.
> 
> Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
> 
> **Note**: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

## brute force solution

```
class Solution(object):
    def mySqrt(self, x):
        
        i=0
      
        while i*i < x:
            i += 1
            
        if i*i == x:
            return i
        else:
            return i-1
```

Complexity: O(sqrt n)

## binary search. 

Start from low = 0 and high = x, let mid = (low + high)//2 and compute mid^2. 
If mid^2 < x^2, update low = mid; if mid^2 > x^2, update high = mid; if mid^2 = x^2, return mid.
Do this until either mid^2 = x^2, or high - low = 1. In the latter case, return high if high^2 = x^2 and else, return low.

```
class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 0
        high = x
        mid = (low+high)//2
        
        while high - low > 1:
            if mid*mid == x:
                return mid
            if mid*mid < x:
                low = mid
                mid = (low+high)//2
            if mid*mid > x:
                high = mid
                mid = (low+high)//2        
        
        if high*high == x:
            return high
        else:
            return low
```            

Complexity: O(log n)
