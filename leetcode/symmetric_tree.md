# symmetric tree (leetcode 101)

https://leetcode.com/problems/symmetric-tree/

## solution: recursive

Base cases:
* if the root has no child nodes, return true;
* if one of the child nodes is null, return false;
* if the values of the two child nodes are not equal, return false.

We can define a helper function that takes two nodes as inputs. 
These two nodes are located on the symmetric positions of the tree.

```
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:       
        
        def recur(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            else:
                if node1.val != node2.val:
                    return False
                return recur(node1.left, node2.right) and recur(node1.right, node2.left)
            
        return recur(root.left, root.right)
```
