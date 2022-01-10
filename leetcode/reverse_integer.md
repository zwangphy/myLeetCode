# reverse integer (leetcode 7)

https://leetcode.com/problems/reverse-integer/

> Given a signed 32-bit integer `x`, return `x` with its digits reversed. 
> If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

# solution 1

* If the input integer `x` is positive. Following the method of [digit sum](digit_sum.md), we can take out every digit number from its rightmost to leftmost.
Store these numbers in an array, call it `y`. Then the reversed integer is equal to


` 1 * (leftmost digit of x) + 10 * (second leftmost digit of x) + ...`


If the reversed integer is smaller than `pow(2,31)-1`, return the reversed integer.

* If the input integer `x` is negative, return `-self.reverse(-x)`.
* Time complexity: O(log x), space complexity: O(log x).

```
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            y = []
            while x >= 1:
                y.append(x%10)
                x //= 10
            reversed_x = 0
            pow10 = 1
            for i in range(len(y)-1, -1, -1):
                reversed_x += y[i]*pow10
                pow10 *= 10
            return reversed_x if reversed_x < pow(2,31)-1 else 0
        
        if x == 0:
            return 0
        
        if x < 0:
            return -self.reverse(-x)
```

## solution 2

We can improve solution 1 by reducing space complexity. We can in fact get the digit of `x` and calculate the reversed number at same time
without introduing an auxillary array.

```
while x != 0:
    digit = x % 10
    reversed_x = reversed_x * 10 + digit
    x //= 10
```

## solution 3

We can call the function `str()` to convert `x` to a string and directly reverse it. Then call the function `int()` to convert the string
to integer.

```
class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        elif x > 0:
            reversed_x = int(str(x)[::-1])
            if reversed_x > pow(2,31)-1: 
                return 0
            else:
                return reversed_x
       
        elif x < 0:
            return -self.reverse(-x)
```

# palindrome number (leetcode 9)

https://leetcode.com/problems/palindrome-number/

## solution

* If the input integer is negative, it's not a palindrome
* If it's positive and is a multiple of 10, it's not a palindrome
* If 0 <= x < 10, it's a palindrome
* Otherwise, use the method of reversing an integer to check if `reversed_x == x`.
