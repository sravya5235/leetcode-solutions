# Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        # Step 1: Create new nodes and insert them next to original nodes
        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next
        
        # Step 2: Assign random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the two lists
        current = head
        copy_head = head.next
        
        while current:
            copy = current.next
            current.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            current = current.next
        
        return copy_head