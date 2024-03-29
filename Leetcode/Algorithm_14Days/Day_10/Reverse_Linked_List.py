#problem : https://leetcode.com/problems/reverse-linked-list/
#problem code: 206
#difficulty: Easy


#----------------------------------Iterative------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head
        while current!=None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        return prev
        

"""
Efficiency:
  Runtime: 30 ms, faster than 97.55% of Python3 online submissions for Reverse Linked List.
  Memory Usage: 15.4 MB, less than 94.91% of Python3 online submissions for Reverse Linked List.
"""





#----------------------------------Using Stack------------------------------------------


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        else:
            stack=deque()
            p=head
            while p!=None:
                stack.append(p)
                p=p.next
            p=head=stack.pop()
            while stack:
                p.next=stack.pop()
                p=p.next
            p.next=None
        return head

"""
Efficiency:    
    Runtime: 24 ms, faster than 99.88% of Python3 online submissions for Reverse Linked List.
    Memory Usage: 15.6 MB, less than 28.62% of Python3 online submissions for Reverse Linked List.
"""
