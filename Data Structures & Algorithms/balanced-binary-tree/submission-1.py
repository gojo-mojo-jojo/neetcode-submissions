# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #[True/False, height]
        def getheight (node):
            if not node:
                return [True, 0]

            left = getheight(node.left)
            right = getheight(node.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, max(left[1], right[1]) + 1] 

        return getheight(root)[0]

        

        