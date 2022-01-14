# Majority element (Leetcode 169)

https://leetcode.com/problems/majority-element/

> Given an array nums of size n, return the majority element. 
> The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

## Solution

Build a dictionary `count` to store the frequency of every element in the input array. There are a few ways to do this.

* Initialize a dictionary whose keys are elements of the input array and all their values are zero (by comprehension). 
  Loop the input array, increment the corresponding value in the dictionary by one.
```
count = {number: 0 for number in nums}
for i in range(len(nums)):
    count[nums[i]] += 1
```

* Create an empty dictionary. Loop the input array. 
  For every number not in the dictionary, add it to the dictionary and assign its value to be 1.
  If the number is in the dictionary, increment its corresponding value in the dictionary by 1.
```
count = {}
for i in range(len(nums)):
    if nums[i] not in count:
        count[nums[i]] = 1
    else:
        count[nums[i]] += 1
```  

* The second method can be written more compactly as
```
count = {}
for i in range(len(nums)):
    count[nums[i]] = count.get(nums[i], 0) + 1
```  
The function `.get(key, x)` returns the value of the specified key in a dictionary. 
If the key is not in the dictionary, return the second argument `x`.

___

Now, let's move forward to the solution. As we loop the input array and increment the value in the dictionary, 
if any value exceeds `len(nums)/2`, the corresponding key is the majority element.

```
class Solution(object):
    def majorityElement(self, nums):
        
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
            
            if count[nums[i]] > len(nums)/2:
                return nums[i] 
```

___

If the majority element is not gaurenteed to be > n/2, we must completely append the frequency of all elements to the dictionary. 
After that, 
```
return max(count,key=count.get)
```
