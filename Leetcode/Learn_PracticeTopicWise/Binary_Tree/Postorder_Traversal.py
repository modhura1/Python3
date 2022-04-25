#https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
#problem : https://leetcode.com/problems/binary-tree-postorder-traversal/
#Difficulty : Easy
#problem code : 145


#------------------------------------Recursive-----------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
      
"""
Efficiency :
  Runtime: 29 ms, faster than 89.15% of Python3 online submissions for Binary Tree Postorder Traversal.
  Memory Usage: 13.8 MB, less than 97.42% of Python3 online submissions for Binary Tree Postorder Traversal.
"""
