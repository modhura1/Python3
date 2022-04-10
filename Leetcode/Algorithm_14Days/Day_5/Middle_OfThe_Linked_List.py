#problem: https://leetcode.com/problems/middle-of-the-linked-list/
#problem code: 876
#difficulty: Easy


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next != None:
            m = head.next
            l = head.next.next
            if l != None:
                while l.next != None:
                    if l.next.next != None:
                        m = m.next
                        l = l.next.next
                    else:
                        m = m.next
                        l = l.next
                        break
            return m
        else:
            return head
        
""" Efficiency:
  Runtime: 46 ms, faster than 43.37% of Python3 online submissions for Middle of the Linked List.
  Memory Usage: 13.9 MB, less than 12.52% of Python3 online submissions for Middle of the Linked List."""


#------------------------------------Approach 2----------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
        #     return slow.next
        return slow
      
""" Efficiency:
  Runtime: 32 ms, faster than 87.15% of Python3 online submissions for Reverse String.
  Memory Usage: 13.8 MB, less than 58.58% of Python3 online submissions for Reverse String."""
