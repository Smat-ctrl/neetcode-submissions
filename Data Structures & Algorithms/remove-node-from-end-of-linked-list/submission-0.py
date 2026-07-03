# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current =  current.next
        
        ignoreIdx = len(arr) - n

        dummy = ListNode()
        curr = dummy
        idx = 0
        while idx < len(arr):
            if idx == ignoreIdx:
                idx += 1
                continue
            nxt = ListNode()
            nxt.val = arr[idx]
            nxt.next = None 
            curr.next = nxt
            curr = curr.next
            idx += 1
        return dummy.next
