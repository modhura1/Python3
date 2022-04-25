#https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
#problem : https://leetcode.com/problems/binary-tree-preorder-traversal/
#Difficulty : Easy
#problem code : 144



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
      
      
"""
Efficiency :
  Runtime: 37 ms, faster than 64.98% of Python3 online submissions for Binary Tree Preorder Traversal.
  Memory Usage: 13.9 MB, less than 62.09% of Python3 online submissions for Binary Tree Preorder Traversal.
"""
