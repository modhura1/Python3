#problem: https://leetcode.com/problems/binary-search/
#problem code: 704
#Difficulty: Easy

class Solution:    
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
        return -1    
    
    
/*Efficiency: 
    Runtime: 541 ms, faster than 5.00% of Python3 online submissions for Binary Search.
    Memory Usage: 15.4 MB, less than 97.81% of Python3 online submissions for Binary Search.*/
