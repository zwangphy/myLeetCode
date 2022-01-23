# letter combination of a phone number (leetcode 17)

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## solution: backtracking/DFS

First of all, we need to create a dictionary that dictates how a number maps to letters. 
To exhaust all the possible letter combinations, it's most convenient to use the method of backtracking/DFS employed in a recursive way.

For example, say the input is `digits = "23"`. At the first step, we append `"a"` to an empty list `out`. Next, we visit the next number
of the input, i.e. `3`, and append `"d"` to `out`. This gives one combination `out = ["a", "d"]`. Next we pop out `"d"` and append `"e"`, 
and then pop out `"e"` and append `"f"`. Now we have exhausted all the possible letter combinations starting with `"a"`. So we only need to loop 
this procedure for all the letters that `"2"` maps to. Recursively, we can define a function and run it for every next letter in `digits`. 

```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        res = []
        def backtrack(s, out=[]):
            #if len(out) == len(digits):
            if len(s) == 0:
                res.append(''.join(out))
                return 
            
            for char in dic[s[0]]:
                out.append(char)
                backtrack(s[1:], out)
                out.pop()
        
        backtrack(digits)
        return res
```
