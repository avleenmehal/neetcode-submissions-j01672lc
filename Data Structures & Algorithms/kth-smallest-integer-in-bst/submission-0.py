# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # res = 0
        # def dfs(root, counter):
        #     if not root:
        #         return 0
        #     if counter
        #     counter+=1
        #     dfs(root.left, counter)
        #     dfs(root.right, counter)
        ans = []
        def dfs(root):
            nonlocal ans
            if not root:
                return
            
            
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        print(ans)

        return ans[k-1]
            
            



            
            
      
        