# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        q = deque([root])
        
        while q:
            sub = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    sub.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    sub.append(node.right.val)
            if sub:
                res.append(sub)
        return res

