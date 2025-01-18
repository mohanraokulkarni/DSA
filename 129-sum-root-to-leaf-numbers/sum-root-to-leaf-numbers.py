# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def root_to_leaf_sum(root,num):
            if not root:
                return 0
            if not root.left and not root.right:
                return num*10 + root.val
            return root_to_leaf_sum(root.left,num *10+root.val) + root_to_leaf_sum(root.right,num *10+root.val)

        return root_to_leaf_sum(root,0)
        
                
        