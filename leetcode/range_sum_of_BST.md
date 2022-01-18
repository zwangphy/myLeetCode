# range sum of BST (leetcode 938)

https://leetcode.com/problems/range-sum-of-bst/

> Given the `root` node of a binary search tree and two integers `low` and `high`, 
> return the sum of values of all nodes with a value in the inclusive range `[low, high]`.

## solution: preorder traversal

Traverse all the nodes of the tree, add its value if it's in the range. We can use any traversal method we like.

```
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def inRange(x, a=low, b=high):
            return a <= x <= b
        
        self.rangeSum = 0
        
        def traversal(node):
            if node:
                if inRange(node.val):
                    self.rangeSum += node.val
                traversal(node.left)
                traversal(node.right)
        
        traversal(root)
        return self.rangeSum
```
