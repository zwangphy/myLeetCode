# maximum depth of binary tree (leetcode 104)

https://leetcode.com/problems/maximum-depth-of-binary-tree/

## recursive solution

Base cases: a null root has zero length; 
a root with no children nodes has length = one.

```
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
```
