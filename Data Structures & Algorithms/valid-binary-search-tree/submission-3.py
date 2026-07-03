# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])
        
        while q:
            for i in range(len(q)):
                node, low, high = q.popleft()

                if not (low < node.val < high):
                    return False

                if node.right:
                    q.append((node.right, node.val, high))

                if node.left:
                    q.append((node.left, low, node.val))
        
        return True