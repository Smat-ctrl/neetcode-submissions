# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        q = deque([root])

        while q:
            furthestFromRight = False
            for i in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                    if not furthestFromRight:
                        res.append(node.right.val)
                        furthestFromRight = True
                if node.left:
                    q.append(node.left)
                    if not furthestFromRight:
                        res.append(node.left.val)
                        furthestFromRight = True
        
        return res
            
