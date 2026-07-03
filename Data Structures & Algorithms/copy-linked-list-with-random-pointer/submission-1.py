"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val) # create a new Node with the same val
            oldToCopy[curr] = copy # save the old copy curr and map it to the new shallow copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToCopy[curr] # Search for the copy from current idx
            copy.next = oldToCopy[curr.next] # Search for the copy for the next of it 
            copy.random = oldToCopy[curr.random] # Search for the copy for the random pointer
            curr = curr.next # advance
        
        return oldToCopy[head] # find the copy of the head

