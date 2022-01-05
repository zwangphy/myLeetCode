# substrings of identical characters

Given a non-empty string `S`, return the number of substrings that contain identical characters only.

The string `S` is made of lower case letters only.

Example: `S = aab`, return 4 because there are two `a`'s, one `aa` and one `b`.

## solution 1: brute force

For every `0 <= i <= len(S) - 1` and `j >= i`, check if `S[j] == S[i]`. If yes, the number of valid substrings increase by 1. If no, reset `i` by `i+1`.

Time complexity: O(n^2)

```
def f(S):
    
    res = 0
    
    for i in range(len(S)):
        for j in range(i,len(S)):
            if S[j] == S[i]:
                res += 1
            else:
                break
    return res
```

## solution 2: sliding window

Consider a string `n` identical characters. We can in fact directly compute the number of valid substrings by ` n(n+1)/2`. This is because
there are n substrings with length one, n-1 substrings with length two, ..., one string with length n.

Back to the general case. If all character between `S[i]` and `S[j]` are found to be identical, 
we can directly compute the number of valid subtrings between `i` and `j` by the formula and then reset `i` by `j+1`.

Time complexity: O(n)

```
def f(S):
    
    res = 0
    
    i = 0
    j = 0
    
    while j <= len(S) - 1:
        for j in range(i,len(S)):
            n = j - i
            if S[j] != S[i]:
                res += n*(n+1)/2
                i = j
                break
            if j == len(S) - 1:
                n = j - i + 1
                res += n*(n+1)/2
                return int(res)
```