# longest substring without repeating characteres (leetcode 3)

https://leetcode.com/problems/longest-substring-without-repeating-characters

> Given a string s, find the length of the longest substring without repeating characters.

## solution 1: naive sliding window

From s[i], check if s[j] is in s[i:j] for j > i. 
If yes, the longest substring starting from s[i] is found. Recorad its length and then repeat for s[i+1].

Time complexity: O(n^2)

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        length = 1
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]:
                    length = max(j-i, length)
                    break
                elif j == len(s) - 1:
                    length = max(len(s)-i, length)
        return length
```

## solution 2: improved sliding window

Solution 1 is inefficient because many of the operations are redundant.

Consider an input string `s = abcded`. We can find the longest substring starting from `s[0] = a` is `abcde`. 
Our code will then check if there are longer substrings starting from `s[1] = b`. But that is not necessary.
In fact, we only need to check if there are longer substrings starting from `e`, the character after the repeating character in our previous sliding window.

We can create a dictionary to store character indices. If a repeating character is found, reset the sliding window. 

Time complexity: O(n), space: O(n).

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        length = 1
        dic = {}
        
        window_start = 0
        
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
                length = max(length, i-window_start+1)
            else:                
                window_start = max(window_start, dic[s[i]] + 1)
                dic[s[i]] = i
                length = max(length, i-window_start+1)
        return length
```        
