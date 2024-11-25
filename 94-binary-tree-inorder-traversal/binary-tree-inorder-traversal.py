# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        h=root
        d=[]
        def inorder(h):
            if h:
                inorder(h.left)
                d.append(h.val)
                inorder(h.right)
        inorder(h)
        return d