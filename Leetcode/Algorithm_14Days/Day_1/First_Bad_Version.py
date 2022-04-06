#problem: https://leetcode.com/problems/first-bad-version/
#problem code: 278
#difficulty: Easy

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        res=-1
        while l<=r:
            mid=(l+r)//2
            if isBadVersion(mid) == False:
                l=mid+1
            else:
                res=mid
                r=mid-1
        return res
      
""" Efficiency:
Runtime: 32 ms, faster than 85.03% of Python3 online submissions for First Bad Version.
Memory Usage: 13.9 MB, less than 14.53% of Python3 online submissions for First Bad Version. """
