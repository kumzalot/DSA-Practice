# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init a dummy node to tackle edgecases
        dummy = ListNode(0, head)
        # init fast and slow pointers to create a sliding window
        fast, slow = dummy, dummy
        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        # removing the nth node from the back
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next

        