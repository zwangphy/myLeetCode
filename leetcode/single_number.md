# single number (leeetcode 136)

https://leetcode.com/problems/single-number/

> Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
> You must implement a solution with a linear runtime complexity and use only constant extra space.

## solution: hash table

This solution is similar to the previous one, [majority element](/leetcode/majority_element.md). 
Use a dictionary to store the frequency of all numbers in the input array. 
Scan the dictionary and return the key whose value is one.

Time complexity: O(n), space O(n)

```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            
        for num in dic.keys():
            if dic[num] == 1:
                return num
```

## solution: bitwise manipulation

https://leetcode.com/problems/single-number/discuss/1682200/Python-solution-using-XOR-bits-116-ms-faster-than-99.54-with-comments
