"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda c:c.start)
        if n==0:
            return 0
        minheap = []
        # minheap.append(intervals[0])
        heapq.heappush(minheap, intervals[0].end)
        rooms = 1
        for i in range(1,n):
            currInt = intervals[i]
            if currInt.start < minheap[0]:
                heapq.heappush(minheap,currInt.end)
                rooms = max(rooms, len(minheap))
            else:
                heapq.heappop(minheap)
                heapq.heappush(minheap,currInt.end)
            
        return rooms
