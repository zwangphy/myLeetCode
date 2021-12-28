# two sum (leetcode 1)

https://leetcode.com/problems/two-sum/

> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
> You can return the answer in any order.

## solution 1 (brute force)

Compute the sum of every pair. 

Time complexity: O(n)

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
```

## solution 2 (two pointer)

*If the array is sorted*, set up two pointers, i from the first element and j from the last element. If `nums[i] + nums[j] < target`, reset i to i+1; 
if `nums[i] + nums[j] > target`, reset j to j-1.

Time complexity: O(n)

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        while i != j:
            if nums[i] + nums[j] < target:
                i += 1
            if nums[i] + nums[j] > target:
                j -= 1
            if nums[i] + nums[j] == target:
                return i,j
```

In general, *if the array is not sorted*, sorting requires O(n logn) time complexity. Furthermore, you need to be very careful 
because the problem asks us to return the indices not the elements.  

### solution 3 (hash table)

time complexity: O(n), space complexity: O(n)

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else: 
                return i, dic[target - nums[i]]
```

exercise problem: why the following code is unsuccessful?
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
            if target - nums[i] in dic:
                return dic[nums[i]], dic[target - nums[i]]
```

Input: [3, 2, 4]

Expected output: 1, 2

Actual output: 0, 0
