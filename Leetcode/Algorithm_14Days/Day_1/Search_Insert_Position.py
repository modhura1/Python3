#problem: https://leetcode.com/problems/search-insert-position/submissions/
#problem code: 35
#Difficulty: Easy

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r=len(nums)
        if nums[-1]<target:
            return r
        if nums[0]>=target:
                return 0
        if r==2:
            return 1
        l=0
        h=r-1
        res=0
        while l<=h:
            m=(l+h)//2
            temp=nums[m]
            if temp==target:
                return m
            elif temp>target:
                h=m-1
            else:
                l=m+1
        if temp<target:
            return m+1
        else:
            return m
        
    
    
/*Efficiency: 
    Runtime: 81 ms, faster than 31.41% of Python3 online submissions for Search Insert Position.
    Memory Usage: 14.7 MB, less than 85.84% of Python3 online submissions for Search Insert Position.*/
