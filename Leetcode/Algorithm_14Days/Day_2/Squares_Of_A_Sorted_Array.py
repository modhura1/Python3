#problem: https://leetcode.com/problems/squares-of-a-sorted-array/
#problem code: 977
#difficulty: Easy

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i,n in enumerate(nums):
            nums[i]=n*n
        return sorted(nums)
      
""" Efficiency:
  Runtime: 224 ms, faster than 92.39% of Python3 online submissions for Squares of a Sorted Array.
  Memory Usage: 15.8 MB, less than 90.23% of Python3 online submissions for Squares of a Sorted Array. """




#------------------------------------Another approach----------------------------------
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[n*n for n in nums]
        return sorted(nums)
