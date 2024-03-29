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



#---------------------------------Approach 3---------------------------------------

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=0
        for j in nums:
            i=i^j
        return i

"""
Efficiency:
    Runtime: 152 ms, faster than 72.63% of Python3 online submissions for Single Number.
    Memory Usage: 16.7 MB, less than 53.84% of Python3 online submissions for Single Number.
"""



#---------------------------------Approach 4---------------------------------------

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            res=nums.pop(i)
            if res in nums:
                nums.remove(res)
                i=0
            else:
                return res

"""
Efficiency:
    Runtime: 2369 ms, faster than 10.64% of Python3 online submissions for Single Number.
    Memory Usage: 15.9 MB, less than 99.79% of Python3 online submissions for Single Number.
"""
