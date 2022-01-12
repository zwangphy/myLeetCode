# preorder, postorder, inorder traversal of binary trees

# preorder

recursive method:

```
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.stack = []
        
        def traversal(node):
            if node:
                self.stack.append(node.val)
                traversal(node.left)
                traversal(node.right)
            
        traversal(root)
        return self.stack
```

iterative:

```
class Solution:
	def preorderTraversal(self, root):
		preorder = []
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				preorder.append(node.val)
				stack.append(node.right)
				stack.append(node.left)
		return preorder
```

## inorder

recursive:

```
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if node:
                inorder(node.left)
                stack.append(node.val)
                inorder(node.right)
            
        stack = []
        inorder(root)
        return stack
```

iterative:

```
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        inorder = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        
        return inorder
```

## postorder

recursive:

```
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                stack.append(node.val)
            
        stack = []
        postorder(root)
        return stack
```
