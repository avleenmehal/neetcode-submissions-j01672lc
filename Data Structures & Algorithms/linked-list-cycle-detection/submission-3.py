# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp = fp = head

        # while sp and sp.next and fp.next and fp.next.next:
        while fp and fp.next:
            sp = sp.next
            fp=fp.next.next
            if sp == fp:
                return True
        
        return False

        