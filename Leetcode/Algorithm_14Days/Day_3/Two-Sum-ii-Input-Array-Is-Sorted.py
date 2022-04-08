#problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#problem code: 167
#difficulty: Medium


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[0,0]
        a=b=c=0
        for i in numbers:
            t=target-i
            sub=numbers[c+1:]
            if t in sub:
                a=c
                b=sub.index(t)+c+1
                break
            c+=1
        res[0]=a+1
        res[1]=b+1
        return res
            
""" Efficiency:
  Runtime: 8600 ms, faster than 5.03% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
  Memory Usage: 15 MB, less than 12.96% of Python3 online submissions for Two Sum II - Input Array Is Sorted."""


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
