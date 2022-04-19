#problem : https://leetcode.com/problems/reverse-bits/
#problem code: 190
#difficulty: Easy


#using .format()
class Solution:
    def reverseBits(self, n: int) -> int:
        #The 0 in 08b is part of the format specification. See the documentation here. If you want zero padding, do '{0:016b}'.format(6) or '{0:032b}'.format(6).
        return int("{:032b}".format(n)[::-1],2)
"""
Efficiency:
  Runtime: 20 ms, faster than 99.89% of Python3 online submissions for Reverse Bits.
  Memory Usage: 13.7 MB, less than 95.03% of Python3 online submissions for Reverse Bits.
"""



#---------------------------------Approach 2---------------------------------------

#using str()
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(bin(n))[2:][::-1].ljust(32,'0') , 2)"""
Efficiency:
    Runtime: 32 ms, faster than 91.22% of Python3 online submissions for Reverse Bits.
  Memory Usage: 13.7 MB, less than 95.03% of Python3 online submissions for Reverse Bits.
"""
