# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. find the meeting point in the LL if a cycle exists
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None

        # 2. reset slow to head and move slow and fast until they meet as cycle exists
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow