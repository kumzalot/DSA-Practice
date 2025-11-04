# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find midpoint
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        # 2. reverse second LL
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. reordering the LL
        t1, t2 = first, second = head, prev
        while t2:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
