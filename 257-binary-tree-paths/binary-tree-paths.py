# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        a=str(root.val)
        ls=[]
        
        def dfs(root,a):
            if not root.left and not root.right:
                ls.append(a)
                return 
            
            if root.left:
                dfs(root.left,a + "->"+ str(root.left.val))
            
            if root.right:
                dfs(root.right,a + "->" + str(root.right.val))
    
        dfs(root,a)
        
        
        return ls

            
        