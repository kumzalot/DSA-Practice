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
        # 1. create a hashmap and map the old nodesto the new ones.
        curr = head
        nodes = {None:None}
        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next

        # 2. complete deep copy by iterating again and mapping resp values
        curr = head
        while curr:
            copy = nodes[curr]
            copy.next = nodes[curr.next]
            copy.random = nodes[curr.random]
            curr = curr.next
        
        return nodes[head]