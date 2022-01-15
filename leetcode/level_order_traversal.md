# level order traversal

## BFS

Starting from the root, we visit its left and right nodes. Store their values to a list `traversal`, to be appended to the output list `res`. 
Also we store these two nodes to a list `nextsearch`. In the next iteration, we will visit all the nodes in `nextsearch`, store the values of
their children nodes in `traversal` (to be appended to `res`) and the position of children nodes in `nextsearch`. The program ends when there are
no nodes in `nextsearch` to visit.

```
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        search = [root]
        while len(search) > 0:
            traversal = []
            nextsearch = []
            for node in search:
                if node.left:
                    traversal.append(node.left.val)
                    nextsearch.append(node.left)
                if node.right:
                    traversal.append(node.right.val)
                    nextsearch.append(node.right)
            if len(traversal) > 0:
                res.append(traversal)
            search = nextsearch
        return res
```
