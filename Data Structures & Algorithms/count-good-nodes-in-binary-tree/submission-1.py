# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()

        queue.append(root)
        ans = 1
        while queue:
            print(queue)
            node = queue.popleft()
            if node:
                if node.left:
                    if node.val <= node.left.val:
                        ans += 1
                        print("ans + 1 ")
                        queue.append(node.left)

                    else: 
                        node.left.val = node.val
                        queue.append(node.left)
                if node.right:
                    if node.val <= node.right.val:
                        ans += 1
                        queue.append(node.right)
                    else: 
                        node.right.val = node.val
                        queue.append(node.right)
        
        return ans