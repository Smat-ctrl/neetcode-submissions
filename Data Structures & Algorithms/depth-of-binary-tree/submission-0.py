# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    def dfs(self, root, count) -> int:
        m1 = 0
        m2 = 0
        if not root:
            return count
        count += 1
        m1 = self.dfs(root.left, count)
        m2 = self.dfs(root.right, count)
        return max(m1, m2)
