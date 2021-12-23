# longest common prefix (leetcode 14)

https://leetcode.com/problems/longest-common-prefix/

> Write a function to find the longest common prefix string amongst an array of strings. 
> If there is no common prefix, return an empty string "".

## solution 1: brute force

Let's sort the list first, so `strs[0]` is the shortest string in the list. 
Then we check if `strs[0][0] == strs[i][0]` for all other i, and subquently if `strs[0][1] == strs[i][1]`...

Time complexity: sorting requires O(n logn) with n = length of the list; algorithm requires O(nm) with m = length of the longest common prefix.
If logn < m, total time copmlexity O(nm); if logn > m, total complexity O(n logn).

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

Follow-up question: how to implement this idea without using .sort() ?

## solution 2: 
