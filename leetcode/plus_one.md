# plus one (leetcode 66)

https://leetcode.com/problems/plus-one/

> You are given a large integer represented as an integer array digits, where each `digits[i]` is the i-th digit of the integer. 
> The digits are ordered from most significant to least significant in left-to-right order. 
> The large integer does not contain any leading 0's.

> Increment the large integer by one and return the resulting array of digits.

# solution (brute force)

Idea: if the last element of the array is not 9, we can simply add one to that element and return the array. If it is 9, 
we replace all neighboring 9's by 0's until we see an element that's not 9 (and add one to that element). 
Eventually, if every element is 9, our methods still worls except that we have to join a list `[1]` to the left.

```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        res = digits[:]
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                res[i] = 0
                if digits[i-1] != 9:
                    res[i-1] += 1
                    return res
                else:
                    res[i-1] = 0
        return [1] + res
```

## solution (recursion)

If the last element is 9, we replace it by 0 and the remaining part is really `plusOne(digits[:-1])`. 
Therefore we can use recursion to write the required program.

```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        if digits == [9]:
            return [1, 0]           
        if digits[-1] < 9:
            digits[-1] +=1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]
```
