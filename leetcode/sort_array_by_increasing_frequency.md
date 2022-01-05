# sort array by increasing frequency (leetcode 1636)

https://leetcode.com/problems/sort-array-by-increasing-frequency/

> Given an array of integers `nums`, sort the array in increasing order based on the frequency of the values. I
> f multiple values have the same frequency, sort them in decreasing order.

> Return the sorted array.

## solution

Use two keys to sort the array, the frequency and the value.

```
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = {x: 0 for x in nums}
        for x in nums:
            dic[x] += 1
        
        nums.sort(key = lambda x: (dic[x], -x))
        return nums
```
