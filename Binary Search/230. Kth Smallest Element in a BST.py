# In-order Traversal
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.tree_list = []
        
        self.inOrder(root)
        if k <= 0:
            return None
        
        print(self.tree_list)
        return self.tree_list[k-1]
    
    def inOrder(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.tree_list.append(root.val)
            return
        
        self.inOrder(root.left)
        self.tree_list.append(root.val)
        self.inOrder(root.right)
        
# In-order Iterative
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
