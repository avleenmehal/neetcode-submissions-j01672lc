# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next

        secondHead = slow.next
        slow.next = None
        prev = None

        while secondHead:
            temp = secondHead.next
            secondHead.next = prev
            prev= secondHead
            secondHead = temp
        
        curr = head
        while curr and prev:
            temp1 = curr.next
            temp2=prev.next
            curr.next=prev
            prev.next=temp1
            curr = temp1
            prev =temp2
        


        