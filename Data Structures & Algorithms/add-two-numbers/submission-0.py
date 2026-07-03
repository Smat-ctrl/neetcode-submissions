# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        overflow = 0
        
        while l1 or l2 or overflow:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sumOf = val1 + val2 + overflow
            digit = sumOf % 10
            overflow = sumOf // 10

            tmp = ListNode(digit)
            cur.next = tmp
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
            

