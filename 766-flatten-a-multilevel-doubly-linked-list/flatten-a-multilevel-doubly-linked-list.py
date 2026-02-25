"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def child(self,node,bottom,nexx):
        curr=bottom
        while curr.next:
            if curr.child:
                self.child(curr,curr.child,curr.next)
            curr=curr.next
        node.next=bottom
        bottom.prev=node
        node.child=None
        curr.next=nexx
        if nexx:
            nexx.prev=curr
        
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        temp=head
        while temp:
            if temp.child:
                nexx=temp.next
                self.child(temp,temp.child,nexx)
            temp=temp.next
        return head