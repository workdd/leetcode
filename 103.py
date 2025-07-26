# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        depth = 0
        while queue:
            res = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if res:
                if depth % 2 != 0:
                    res = res[::-1]
                result.append(res)
            depth += 1

        return result
