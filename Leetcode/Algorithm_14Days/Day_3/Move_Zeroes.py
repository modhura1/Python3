#problem: https://leetcode.com/problems/move-zeroes/
#problem code: 283
#difficulty: Easy


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sum(nums)!=0 and nums.count(0)>0:
            l=len(nums)
            if l==2:
                if nums[0]==0:
                    nums[0]=nums[1]
                    nums[1]=0
            else:
                f=l
                for i in range(l-1,0,-1):
                    if nums[i]!=0:
                        break
                    else:
                        f-=1
                
                writeTo=0
                for i in range(f):
                    if nums[i]!=0:
                        nums[writeTo]=nums[i]
                        writeTo+=1

                while writeTo < f:
                    nums[writeTo]=0
                    writeTo+=1
            
""" Efficiency:
  Runtime: 168 ms, faster than 93.22% of Python3 online submissions for Move Zeroes.
  Memory Usage: 15.6 MB, less than 70.50% of Python3 online submissions for Move Zeroes."""


#--------------------------------------Another Approach-------------------------

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sum(nums)!=0:
            l=len(nums)
            i=0
            while i<l:
                if nums[i]==0:
                    nums.pop(i)
                    nums.append(0)
                    i=0
                    l-=1
                else:
                    i+=1
      
""" Efficiency:
  Runtime: 3628 ms, faster than 5.00% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.5 MB, less than 70.50% of Python3 online submissions for Move Zeroes."""
