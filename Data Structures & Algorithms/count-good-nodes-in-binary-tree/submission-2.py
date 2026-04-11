# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        ans = 0

        def dfs(root, maxV):
            nonlocal ans
            if not root:
                return
            if root.val >= maxV:
                ans+=1
                maxV = root.val

            dfs(root.left, maxV)
            dfs(root.right, maxV)

        dfs(root,root.val)
        return ans

        # if not root:
        #     return 0

        # ans = 0 
        # queue = collections.deque()
        # queue.append(root)
        # ans+=1

        # while queue:

        #     node = queue.popleft()

        #     if node.left:
        #         if node.val>node.left.val:
        #             node.left.val = node.val
                    
        #         else:
        #             ans+=1
        #         queue.append(node.left)
            
        #     if node.right:
        #         if node.val>node.right.val:
        #             node.right.val = node.val
                    
        #         else:
        #             ans+=1
        #         queue.append(node.right)


        # return ans
        
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         queue = deque()

#         queue.append(root)
#         ans = 1
#         while queue:
#             print(queue)
#             node = queue.popleft()
#             if node:
#                 if node.left:
#                     if node.val <= node.left.val:
#                         ans += 1
#                         print("ans + 1 ")
#                         queue.append(node.left)

#                     else: 
#                         node.left.val = node.val
#                         queue.append(node.left)
#                 if node.right:
#                     if node.val <= node.right.val:
#                         ans += 1
#                         queue.append(node.right)
#                     else: 
#                         node.right.val = node.val
#                         queue.append(node.right)
        
#         return ans