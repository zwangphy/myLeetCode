# merge intervals (leetcode 56)

https://leetcode.com/problems/merge-intervals/

> Given an array of `intervals` where `intervals[i] = [start, end]`, merge all overlapping intervals, 
> and return an array of the non-overlapping intervals that cover all the intervals in the input.

## solution

Sort the input array so intervals with smaller start values appear first. In this way, if `intervals[i+1]` does not overlap
with `intervals[i]`, all intervals after i+1 do not overlap with `intervals[i]` neither.

The algorithm to solve this problem is as follows. For i,
* If `intervals[i+1]` overlaps with `intervals[i]`, replace `intervals[i+1]`in-place by the merged interval. 
* If `intervals[i+1]` does not overlap with `intervals[i]`, append `intervals[i]` to the output
array. 

In the end, we must also append `intervals[-1]` to the output array (regardless of whether or not it overlaps with previous intervals).

```
# returns true if two intervals are non-overlapping
def notOverlap(a,b):
    if a[0] > b[1] or a[1] < b[0]:
        return True
    else:
        return False

# returns the merged interval if two intervals are overlapping 
def Overlap(a,b):
    if not notOverlap(a,b):
        return [min(a[0], b[0]), max(a[1], b[1])]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return [intervals[0]]  
        
        intervals.sort(key = lambda x: x[0])
        res = []     
        
        for i in range(1, len(intervals)):
            if not notOverlap(intervals[i], intervals[i-1]):
                intervals[i] = Overlap(intervals[i-1], intervals[i])
            if notOverlap(intervals[i], intervals[i-1]):    
                res.append(intervals[i-1])
                
        res.append(intervals[-1])  
        
        return res
```
