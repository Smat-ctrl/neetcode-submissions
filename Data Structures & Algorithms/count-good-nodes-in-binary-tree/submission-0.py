# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
        
    def dfs(self, root, rootVal) -> int:
        if not root:
            return 0
        count = 0
        if root.val >= rootVal:
            count = 1
        rootVal = max(root.val, rootVal)
        left = self.dfs(root.left, rootVal)
        right = self.dfs(root.right, rootVal)
        return count + left + right