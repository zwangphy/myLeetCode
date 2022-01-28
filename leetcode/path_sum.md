# path sum I (leetcode 112)

https://leetcode.com/problems/path-sum/

## solution: recursive

```
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recur(node, num):
            if not node:
                return False
            if node:
                if not node.left and not node.right and num == node.val: 
                    return True
                else:
                    return recur(node.left, num-node.val) or recur(node.right, num-node.val)
        return recur(root, targetSum)
```

# path sum II (leetcode 113)

https://leetcode.com/problems/path-sum-ii/

## solution:
