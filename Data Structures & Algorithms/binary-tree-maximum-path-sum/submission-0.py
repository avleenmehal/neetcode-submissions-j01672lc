# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxScore = float("-inf")

        def dfs(root):
            nonlocal maxScore
            if not root:
                return 0
        
            leftTree = max(dfs(root.left),0)
            print("left" , leftTree)

            rightTree= max(dfs(root.right),0)
            print("right", rightTree)

            splitPath = root.val+leftTree+rightTree
            maxScore = max(maxScore, splitPath)
            
            return root.val + max(leftTree, rightTree)
        
        dfs(root)

        return maxScore