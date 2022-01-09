# longest palindromic substring (leetcode 5)

https://leetcode.com/problems/longest-palindromic-substring/submissions/

> Given a string `s`, return the longest palindromic substring in `s`.

## solution 1: brute force

If the length of `s` is n, there is one subtring of length n, two substrings of length n-1, ..., n substrings of length 1.
In total, there are O(n^2) substrings. We can scan every one of them and check if it is palindromic.

Time complexity: O(n^3). Checking whether a substring is palindromic takes O(n) time, and there O(n^2) substrings.

## solution 2: two pointer

A palindromic string can be expanded from its center. For instance, in `xyaxy` every pair of letters at equal distance to `a` are identical.
This is the case of a parlindromic string of odd length. For `xyyx`, every pair of letters from `yy` are identical.

For a string of length n, there are 2n-1 centers. We can go to every center and make the expansion to find the longest parlindromic
string centered at that location. The algo can be implemented by two pointers. One pointer points to the location of the center in the parent string.
The other pointer tracks the distance from the center.

Complexity: O(n^2)

```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        res = s[0]
        for i in range(1,len(s)):
            # if s[i] == s[i-1], here could be the center of an even-length palindrome
            j = 0
            while i+j < len(s) and i-1-j >=0 and s[i+j] == s[i-1-j]:
                if max_len < 2+2*j:
                    max_len = 2+2*j
                    res = s[i-1-j:i+j+1]
                j += 1
            # if s[i+1] == s[i-1], here could be the center of an odd-length palindrome
            j = 0
            while i+1+j < len(s) and i-1-j >=0 and s[i+1+j] == s[i-1-j]:
                if max_len < 3+2*j:
                    max_len = 3+2*j
                    res = s[i-1-j:i+1+j+1]
                j += 1
        return res
```

## solution 3: dp

Let `dp[i,j] = True if s[i,j+1] is palindromic; = False otherwise`. 
Then, `dp[i-1, j+1]` will be True if and only if `dp[i,j]` is True and `s[i-1] == s[j+1]`.

Time complexity: O(n^2)

## solution 4:

There is an algo with O(n) time complexity. Manacher's algorithm.
