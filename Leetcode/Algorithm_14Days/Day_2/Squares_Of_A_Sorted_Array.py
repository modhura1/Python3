#problem: https://leetcode.com/problems/squares-of-a-sorted-array/
#problem code: 977
#difficulty: Easy

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            res.append(i*i)
        res.sort()
        return res
      
""" Efficiency:
  Runtime: 364 ms, faster than 32.24% of Python3 online submissions for Squares of a Sorted Array.
  Memory Usage: 16.3 MB, less than 53.29% of Python3 online submissions for Squares of a Sorted Array. """
