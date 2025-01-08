# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        d=root
        ls=[]
        def preorder(d):
            if d:
                ls.append(d.val)
                preorder(d.left)
                preorder(d.right)
        preorder(d)
        return ls

        