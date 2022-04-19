#problem : https://leetcode.com/problems/single-number/
#problem code: 136
#difficulty: Easy


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
        return l[0]        

"""
Efficiency:
  Runtime: 1543 ms, faster than 13.08% of Python3 online submissions for Single Number.
  Memory Usage: 16.9 MB, less than 14.25% of Python3 online submissions for Single Number.
"""



#---------------------------------Efficient Approach---------------------------------------

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        for j in range(1,len(nums)):
            if nums[i]==nums[j]:
                nums[i]=nums[j]=0
            i+=1
        return sum(nums)
"""
Efficiency:
    Runtime: 198 ms, faster than 45.12% of Python3 online submissions for Single Number.
    Memory Usage: 16.1 MB, less than 99.09% of Python3 online submissions for Single Number.
"""
