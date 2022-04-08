#problem: https://leetcode.com/problems/rotate-array/
#problem code: 189
#difficulty: Medium

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=len(nums)
        if l>1 and k!=0:
            if l==2:
                if k%2==1:
                    nums.reverse()
            else:
                if k>l:
                    k-=l
                nums[:k],nums[k:]=nums[-k:],nums[:-k]
      
""" Efficiency:
  Runtime: 200 ms, faster than 99.67% of Python3 online submissions for Rotate Array.
  Memory Usage: 25.6 MB, less than 7.66% of Python3 online submissions for Rotate Array."""


#--------------------------------------Another Approach-------------------------
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      for i in range(k):
            x=nums.pop()
            nums.insert(0,x)
            
#not time efficient
