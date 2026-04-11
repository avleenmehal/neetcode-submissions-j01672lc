# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     ans = []

    #     queue = deque()
    #     queue.append(root)

    #     while queue:
    #         l = len(queue)
    #         innlist = []
    #         for i in range(l):
    #             node = queue.popleft()
    #             if not node:
    #                 continue
    #             innlist.append(node.val)
    #             queue.append(node.left)
    #             queue.append(node.right)
    #         if innlist:
    #             ans.append(innlist)

    #     finalans = []
    #     for i in range(len(ans)):
    #         finalans.append(ans[i][-1])

    #     return finalans
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res