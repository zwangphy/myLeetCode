# single number (leeetcode 136)

https://leetcode.com/problems/single-number/

> Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
> You must implement a solution with a linear runtime complexity and use only constant extra space.

## solution

```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {num: 0 for num in nums}
        for num in nums:
            dic[num] += 1
        for num in nums:
            if dic[num] == 1:
                return num
```
