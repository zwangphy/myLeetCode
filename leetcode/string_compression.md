# string compression (leetcode 443)

https://leetcode.com/problems/string-compression/

## solution: 3 pointers

Initialize a pointer `i == 0`. Scan every letter `chars[j]` in the input. 
If `chars[j] != chars[j-1]`, we increment `i` by one. 
Namely, `i` is used to track the number of non-repeating letters seen so far.
Use another variable `count` to track the number of consecutive repeating letters.
If `chars[j] == chars[j-1]`, increment `count` by one. 
Otherwise, if `chars[j] != chars[j-1]`, reset `count = 1`.
Also, we need to convert `count` to a string and append this string after a group of consecutive repeating characters.

```
class Solution:
    def compress(self, chars: List[str]) -> int:
        # insert the length of repeating letters as a string
        def insert_cnt(i, cnt):
            for k in range(len(str(cnt))):
                chars[i+1+k] = str(cnt)[k]
        
        if len(chars) == 1:
            return 1
        
        i = 0
        count = 1
        for j in range(1, len(chars)):
            if chars[j] == chars[j-1]:
                count += 1
                if j == len(chars)-1:
                    insert_cnt(i, count)
                    return i+1+len(str(count))
            if chars[j] != chars[j-1]:
                if count == 1:
                    i += 1
                    chars[i] = chars[j]
                else:
                    insert_cnt(i, count)                      
                    i += len(str(count))+1
                    chars[i] = chars[j]
                    count = 1
        return i+1
```
