#https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
#problem : https://leetcode.com/problems/binary-tree-inorder-traversal/
#Difficulty : Easy
#problem code : 94


#------------------------------------Recursive-----------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
      
      
"""
Efficiency :
  Runtime: 34 ms, faster than 74.23% of Python3 online submissions for Binary Tree Inorder Traversal.
  Memory Usage: 13.7 MB, less than 97.24% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
