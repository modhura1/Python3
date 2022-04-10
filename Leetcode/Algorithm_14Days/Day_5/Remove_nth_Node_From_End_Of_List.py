#problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#problem code: 876
#difficulty: Medium


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #checking for single node list
        if head.next==None:
            return None
        
        l = 1
        left,right = head,head
        i = n
        while i>0 and right.next != None:
            right = right.next
            l+=1
            i-=1
        while right.next!=None:
            left = left.next
            right = right.next
            l += 1
        if l==n:
            return (head.next)    
        left.next = left.next.next
        return head
        
""" Efficiency:
  Runtime: 20 ms, faster than 99.95% of Python3 online submissions for Remove Nth Node From End of List.
  Memory Usage: 13.8 MB, less than 74.08% of Python3 online submissions for Remove Nth Node From End of List."""
