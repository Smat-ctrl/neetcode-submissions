# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy

        while True:
            if list1 == None:
                curr.next = list2
                break
            if list2 == None:
                curr.next = list1
                break
            if list1.val < list2.val:
                nxt = ListNode()
                nxt.val = list1.val
                list1 = list1.next
                nxt.next = None
                curr.next = nxt
                curr = curr.next
            else:
                nxt = ListNode()
                nxt.val = list2.val
                list2 = list2.next
                nxt.next = None
                curr.next = nxt
                curr = curr.next
        
        return dummy.next