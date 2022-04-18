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


#------------------------------------Approach 2----------------------------------------------------------
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n==int(n) and n>1:
            n = n/2
        return n==1
"""
Efficiency:
    Runtime: 33 ms, faster than 84.78% of Python3 online submissions for Power of Two.
    Memory Usage: 13.8 MB, less than 95.82% of Python3 online submissions for Power of Two.
"""    


#------------------------------------Approach 3----------------------------------------------------------
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n>1:
            n=n/2
        return n==1
"""
Efficiency:
    Runtime: 25 ms, faster than 97.68% of Python3 online submissions for Power of Two.
    Memory Usage: 13.8 MB, less than 95.82% of Python3 online submissions for Power of Two.
"""
