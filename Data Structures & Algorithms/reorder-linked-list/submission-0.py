# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        arr = []
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next

        curr = head
        left, right = 0, len(arr) - 1
        take_left = True
    
        while curr:
            if take_left:
                curr.val = arr[left]
                left += 1
            else:
                curr.val = arr[right]
                right -= 1
            take_left = not take_left
            curr = curr.next

        

