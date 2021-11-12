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
        """
        :type height: List[int]
        :rtype: int
        """
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
If height[i] < height[j], then by moving j to left we will not find a larger volume! Thus, the only way to find a larger volum is moving i to its right.
Likewise, if height[i] > height[j], we need to move j to left.
