# pascal's triangle I, II (leetcode 118)

https://leetcode.com/problems/pascals-triangle/

## solution

```
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1]+res[i-1][j])
        return res
```

leetcode 119 is essentially identical, except that it requires to return the n-th row of pascal's triangle.
