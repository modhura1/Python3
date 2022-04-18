#problem : https://leetcode.com/problems/number-of-1-bits/
#problem code: 191
#difficulty: Easy


class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)[2:]
        count = 0
        for i in s:
            if i=='1':
                count+=1
        return count
      
      
      
"""
Efficiency:
  Runtime: 25 ms, faster than 96.83% of Python3 online submissions for Number of 1 Bits.
  Memory Usage: 13.7 MB, less than 95.45% of Python3 online submissions for Number of 1 Bits.
"""


#------------------------------------More Efficient Approach----------------------------------------------------------
class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        for i in bin(n)[2:]:
            if i=='1':
                c+=1
        return c
    
"""
Efficiency:
    Runtime: 23 ms, faster than 99.06% of Python3 online submissions for Number of 1 Bits.
    Memory Usage: 13.8 MB, less than 95.45% of Python3 online submissions for Number of 1 Bits.
"""
