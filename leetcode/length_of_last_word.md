# length of last word (leetcode 58)

https://leetcode.com/problems/length-of-last-word/

> Given a string `s` consisting of some words separated by some number of spaces, return the length of the last word in the string.

## solution 1: brute force

Idea: starting from `s[len(s)-1]` and scanning to left, find the first non-white space. This is where the last word ends.
From that index, scan further left and find the first white space (this is where the last word starts) 
or you reach all the way to `s[0]` (there is only one word in the string).

```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
            else:
                end = i
                break
                
        while i > 0:
            if s[i] != ' ':
                i -= 1
            if s[i] == ' ':
                start = i + 1
                return end - start + 1
        
        return end + 1
```

## solution 2: one-line solution with split()

We can also use the built-in function split() to separate the string into a list. By default, split() without any argument will
use white space as separator.

```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
```

Note the subtle difference between `s.split()` and `s.split(' ')`:

![image](https://user-images.githubusercontent.com/88695029/147317522-5f7a809d-8f30-4f17-bd6c-10c0a2e86419.png)


