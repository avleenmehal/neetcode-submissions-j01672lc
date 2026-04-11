# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode(0,l1)
        dummy =res
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            res.next= ListNode(sum%10)
            if sum >=10:
                carry = 1    
            else:
                carry = 0
            res = res.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            print(carry)
            sum = carry + l1.val
            res.next= ListNode(sum%10)
            if sum >=10:
                carry = 1
            else:
                carry = 0
            res=res.next
            l1 = l1.next
        while l2:
            sum = carry + l2.val
            res.next= ListNode(sum%10)
            if sum >=10:
                carry = 1  
            else:
                carry = 0
            res=res.next
            l2 = l2.next
        if carry:
            res.next = ListNode(carry,None)
        
        return dummy.next