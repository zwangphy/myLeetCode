# Container with most water (leetcode 11)

https://leetcode.com/problems/container-with-most-water/

> Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
> n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
> Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

## brute force solution

Loop through every pair i,j in the list and calculate the volume. 

```
class Solution(object):
    def maxArea(self, height):
        
        L = len(height)
        vol = 0
        
        for i in range(L):
            for j in range(i+1,L):
                h = min(height[i],height[j])
                vol = max(vol, (j-i)*h)
        return vol
```

Complexity: O(n^2)

## better solution

Create two indices. One index, i, runs from the leftmost element and the other, j, from rightmost.
If height[i] < height[j], then varying j will not help you find a larger volume. 
We need to move i to the right and along the way keep record of the max volume by far.
At some i', perhaps height[i'] > height[j]. When that happens, we need to move j to the left.

```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        i, j = 0, len(height)-1
        while i < j:
            vol = max(vol, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return vol
```        

Complexity: O(n)
