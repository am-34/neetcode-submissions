# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        prev = None
        current = head
        while current:
            next_node = current.next #next = itr.next
            current.next = prev #itr.next = prev
            prev = current #prev = itr
            current = next_node #itr = itr.next

        self.head = prev
        return prev