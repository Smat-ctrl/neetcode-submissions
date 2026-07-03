# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l = 1
        r = len(arr) - 1
        rightTurn = True

        current = head
        while l <= r:
            tmp = ListNode()
            if rightTurn:
                tmp.val = arr[r]
                tmp.next = None
                head.next = tmp
                head = head.next
                r -= 1
            else:
                tmp.val = arr[l]
                tmp.next = None
                head.next = tmp
                head = head.next
                l += 1
            rightTurn = not rightTurn
        
                