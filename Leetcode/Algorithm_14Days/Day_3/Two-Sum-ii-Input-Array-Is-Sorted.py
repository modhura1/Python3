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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=b=c=0
        for i in numbers:
            t=target-i
            sub=numbers[c+1:]
            if t in sub:
                a=c
                b=sub.index(t)+c+1
                break
            c+=1
        a+=1
        b+=1
        return [a,b]
      
""" Efficiency:
  Runtime: 9696 ms, faster than 5.03% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.9 MB, less than 91.20% of Python3 online submissions for Two Sum II - Input Array Is Sorted."""
