# substring position

> Given a string s, return the min index before which every letter in 'python' has appeared. Return -1 if no such index exists.

## solution

Create a dictionary dic that stores the number of occurance of each letter in 'python'. 
Scan the string; if you see a letter that's in dic, subtract its corresponding value by 1.
When all the values in dic are <= 0, the required position is found.

```
def f(s):
  
    substring = 'python'
  
    dic = {}
    for l in substring:
        if l in dic:
            dic[l] += 1
        else:
            dic[l] = 1
    
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]] -= 1
    
        if all(x <= 0 for x in dic.values()):
            return i
        
    return -1
```      

[//]: # (Note: for l in s: ... return s.index l doesn't work.)      

