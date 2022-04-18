#problem : https://leetcode.com/problems/power-of-two/
#problem code: 231
#difficulty: Easy


import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0:
            s=math.log2(n)
            if int(s)==s:
                return True
            else:
                 return False
        else:
            return False
            
            
"""
Efficiency:
  Runtime: 27 ms, faster than 97.27% of Python3 online submissions for Power of Two.
  Memory Usage: 13.8 MB, less than 56.00% of Python3 online submissions for Power of Two.
"""
