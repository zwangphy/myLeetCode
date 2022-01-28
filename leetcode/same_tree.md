# same tree (leetcode 100)

https://leetcode.com/problems/same-tree/

## solution: recursive

Base cases: 
* if two roots are null, return true; 
* if one root is null and the other is not, return false; 
* if two roots have different values, return false.

```
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

Alternately, we can define a helper function
```
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recur(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (node2 and not node1):
                return False
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                return recur(node1.left, node2.left) and recur(node1.right, node2.right)
                 
        
        return recur(p, q)
```
