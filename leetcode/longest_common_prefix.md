# longest common prefix (leetcode 14)

https://leetcode.com/problems/longest-common-prefix/

> Write a function to find the longest common prefix string amongst an array of strings. 
> If there is no common prefix, return an empty string "".

## solution 1: brute force

Let's sort the list first, so `strs[0]` is the shortest string in the list. 
Then we check if `strs[0][0] == strs[i][0]` for all other i, and subquently if `strs[0][1] == strs[i][1]`...

Time complexity: sorting requires O(n logn) with n = length of the list; comparison of strings requires O(nm) with m = length of the longest common prefix.
Total complexity is the sum of two.

Codes:
```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if strs[i][j] != strs[0][j]:
                    return strs[0][:j]
        return strs[0]
```

Follow-up question: how to implement this algorithm without using sort() ?

## solution 2: 

`min(strs)` and `max(strs)` return lexicographically min and max. We only need to compare these two strings. 
If their first i characters are identical, all the strings between them have same characters up to i-th index.

Time complexity: O(n) to find min and max, O(m) to find the longest common prefix. Total O(n+m).

Codes:
```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        lexmin = min(strs)
        lexmax = max(strs)
        
        idx = min(len(lexmin), len(lexmax))
        
        for i in range(idx):
            if lexmin[i] != lexmax[i]:
                return lexmin[:i]
        
        return lexmin[:idx]
```
