# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        allNodes = []
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                allNodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        diameter = 0
        #now we have all the Nodes
        for node in allNodes:
            diameter = max(diameter, self.dfs(node.left) + self.dfs(node.right))
    
        return diameter
    
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))



        
