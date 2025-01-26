# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            if not l1: # reaches end of LL A.
                l1 = headB
            else:
                l1 = l1.next
            if not l2: # reaches end of LL A.
                l2 = headA
            else:
                l2 = l2.next
        return l1