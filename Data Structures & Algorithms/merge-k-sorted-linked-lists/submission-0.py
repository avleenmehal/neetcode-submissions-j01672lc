# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        dummy = ListNode(0, None)
        prev = dummy

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))

            
        while heap:
            nodeVal,i,node = heapq.heappop(heap)
            prev.next = node

            if node.next:
                heapq.heappush(heap,(node.next.val, i, node.next))
            prev = prev.next
        # print(heap)

        return dummy.next


