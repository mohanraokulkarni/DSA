# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level=0
        def depth(root,level):
            if root:
                l=depth(root.left,level+1)
                r=depth(root.right,level+1)
                return max(l,r)
            else:
                return level
        return depth(root,level)
        