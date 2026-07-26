# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def getheight (node):
            nonlocal res
            if not node :
                return 0
            if not res:
                return 0

            left = getheight(node.left)
            right = getheight(node.right)
            if abs(left - right) > 1:
                res = False
                return 0

            return max(left, right) + 1
        getheight(root)
        return res

        