# Traversal Solution
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        tree_list = []
        self.travsal_tree(root, tree_list)
        return len(tree_list)
    
    def travsal_tree(self, root, tree_list):
        if not root:
            return
        self.travsal_tree(root.left, tree_list)
        tree_list.append(root)
        self.travsal_tree(root.right, tree_list)
  
 # Two pointer solution (同向双指针)
 class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return
        
        left_depth = self.get_depth(root, True)
        right_depth = self.get_depth(root, False)
        
        if left_depth == right_depth:
            return 2 ** left_depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def get_depth(self, root, is_left):
        if root is None:
            return 0
        if is_left:
            return 1 + self.get_depth(root.left, is_left)
        else:
            return 1 + self.get_depth(root.right, is_left)
