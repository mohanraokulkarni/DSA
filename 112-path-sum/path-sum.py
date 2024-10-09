# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        suma=0
        def dfs(root,suma,targetSum):
            if not root:
                return False
            
            suma=suma+root.val
            if (root.left==None and root.right==None) and suma==targetSum:
                return True 

            return dfs(root.left,suma,targetSum) or dfs(root.right,suma,targetSum)
        
                
        return dfs(root,suma,targetSum)
        
