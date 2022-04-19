#problem : https://leetcode.com/problems/single-number/
#problem code: 136
#difficulty: Easy


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
        return l[0]        

"""
Efficiency:
  Runtime: 1543 ms, faster than 13.08% of Python3 online submissions for Single Number.
  Memory Usage: 16.9 MB, less than 14.25% of Python3 online submissions for Single Number.
"""
