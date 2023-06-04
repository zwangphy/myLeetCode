# Trapping rain water (leetocode 42)

https://leetcode.com/problems/trapping-rain-water/description/

## Solution: two pointer

Initialize two pointers, i and j, from the left and right hand side of the array respectively. When moving the pointers,
we also track the current maximum height from the left and right, `l_max` and `r_max`.

If `height[i] < height[j]` and `height[i] < l_max`, this gaurantees that a volume of `l_max - height[i]` can trap water. 
If `height[i] < height[j]` but `height[i] >= l_max`, we update `l_max`. (It's important to keep the `=` sign here. Think about
the case where `height = [1,1,1,1,1,2]`. No water can be stored in this case!) 

```
class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        l_max, r_max = height[0], height[-1]
        water = 0

        while i < j:
            if height[i] < height[j]:
                if height[i] >= l_max:
                    l_max = height[i]
                else:
                    water += l_max - height[i]
                i += 1
            else:
                if height[j] >= r_max:
                    r_max = height[j]
                else:
                    water += r_max - height[j]
                j -= 1
        
        return water
```
