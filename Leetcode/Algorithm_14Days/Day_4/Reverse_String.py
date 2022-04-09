#problem: https://leetcode.com/problems/reverse-string/
#problem code: 344
#difficulty: Easy


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[-1::-1]
        
""" Efficiency:
  Runtime: 192 ms, faster than 98.58% of Python3 online submissions for Reverse String.
  Memory Usage: 18.8 MB, less than 8.22% of Python3 online submissions for Reverse String."""


#------------------------------------Approach 2----------------------------------------------------------

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1
        while l<=r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
            
""" Efficiency:
  Runtime: 196 ms, faster than 96.39% of Python3 online submissions for Reverse String.
  Memory Usage: 18.4 MB, less than 89.68% of Python3 online submissions for Reverse String."""


#--------------------------------------Approach 3------------------------------

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
""" Efficiency:
  Runtime: 361 ms, faster than 14.54% of Python3 online submissions for Reverse String.
  Memory Usage: 18.5 MB, less than 18.91% of Python3 online submissions for Reverse String."""
