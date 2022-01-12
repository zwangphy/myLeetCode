# level order traversal

BFS

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
