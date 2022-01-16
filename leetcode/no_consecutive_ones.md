# binary numbers with no consecutive ones

> Count the number of ways to construct a string of length n. The string is made of 0 and 1 and there are no consecutive `1`'s.

## solution 1: backtracking

Brute force solution: generate all 2^n strings and remove those having consecutive `1`'s. Time: O(n 2^n).

Backtracking: we can print all the valid strings satisfying the constraint recursively. Time: < O(2^n).

```
def validStrings(n, out = '', final_digit='0'):
    
    if n == 0:
        print(out)
        return
    
    
    validStrings(n-1, out+'0', final_digit = '0')
    
    if final_digit != '1':
        validStrings(n-1, out+'1', final_digit = '1')

if __name__ == '__main__':
 
    n = 4
 
    validStrings(n)
```

> 0000
> 0001
> 0010
> 0100
> 0101
> 1000
> 1001
> 1010

If we want to append all valid strings to a list,

```
def countWays(n):
    res = []
    def backtrack(n, out = [], final_digit='0'):
        if n==0:
        #if len(out) == n: # not work because n changes
            res.append(''.join(out))
            return

        out.append('0')
        backtrack(n-1, out, final_digit = '0')
        out.pop()

        if final_digit != '1':
            out.append('1')
            backtrack(n-1, out, final_digit = '1')
            out.pop()
    backtrack(n)
    print(res, len(res))
    

if __name__ == '__main__':
 
    n = 4
 
    countWays(n)
```

> ['0000', '0001', '0010', '0100', '0101', '1000', '1001', '1010'] 8

## solution 2: dp

Let `f(n)` and `g(n)` be the number of length-n valid strings ending with `0` and `1` respectively. 
If a valid string ends with `0`, we can add either `0` or `1` to its end which makes a new valid string of length-(n+1).
If a valid string ends witn `1`, we can only add `0`.
Therefore we have the relation
```
f(n+1) = f(n) + g(n),
g(n+1) = f(n)
```
We can write a dp code for this two-dimensional recurrsion.

In fact, it can be reduced to a one-dimensional recurrsion. Since `g(n) = f(n-1)`, we have
```
f(n+1) = f(n) + f(n-1)
```
for n >= 2.

Note that we need to return the sum of `f(n)` and `g(n)`.
