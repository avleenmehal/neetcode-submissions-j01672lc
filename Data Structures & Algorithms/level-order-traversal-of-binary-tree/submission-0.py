# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        queue = deque()
        queue.append(root)

        while queue:
            l = len(queue)
            innlist = []
            for i in range(l):
                node = queue.popleft()
                if not node:
                    continue
                innlist.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if innlist:
                ans.append(innlist)
        
        return ans
        