#problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/
#problem code: 557
#difficulty: Easy


class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        new = s.split()
        for i in new:
            res = res + " " + i[::-1]
        return (res.lstrip())
        
""" Efficiency:
  Runtime: 32 ms, faster than 95.99% of Python3 online submissions for Reverse Words in a String III.
  Memory Usage: 14.8 MB, less than 15.77% of Python3 online submissions for Reverse Words in a String III."""


#------------------------------------Approach 2----------------------------------------------------------

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        new = s.split()
        for i in new:
            res += " " + i[::-1]
        return (res.lstrip())
      
""" Efficiency:
  Runtime: 36 ms, faster than 90.56% of Python3 online submissions for Reverse String.
  Memory Usage: 14.6 MB, less than 85.52% of Python3 online submissions for Reverse String."""


#--------------------------------------Approach 3------------------------------

class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for i in s.split():
            res.append(i[::-1])
        return (' '.join(res))
            
        
""" Efficiency:
  Runtime: 50 ms, faster than 66.42% of Python3 online submissions for Reverse Words in a String III.
  Memory Usage: 14.7 MB, less than 50.08% of Python3 online submissions for Reverse Words in a String III."""
