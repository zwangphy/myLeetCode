# sort characters by frequency (leetcode 451)

https://leetcode.com/problems/sort-characters-by-frequency/

> Given a string `s`, sort it in decreasing order based on the frequency of the characters. 
> The frequency of a character is the number of times it appears in the string.

> Return the sorted string. If there are multiple answers, return any of them.

## solution

Use a dictionary to store the frequency of characters as a function of characters. 
The function `items()` returns the list of tuple pairs (key, value) of a dictionary. In our case,
```
[(character1, frequency1), (character2, frequency2), ...]
```
Sort the list by frequency and we can construct the sorted string.

```
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        
        res = ''
        for key, value in dic.items():
            res += key * value
        return res
```
