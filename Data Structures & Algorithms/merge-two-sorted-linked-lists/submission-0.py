# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2

        dummy_head = ListNode(val=None, next=None)
        dummy = dummy_head

        while current1 and current2:
            if current1.val <= current2.val:
                dummy.next = current1
                current1 = current1.next
            else:
                dummy.next = current2
                current2 = current2.next
            
            dummy = dummy.next
        
        if current1:
            dummy.next = current1
        else:
            dummy.next = current2

        return dummy_head.next