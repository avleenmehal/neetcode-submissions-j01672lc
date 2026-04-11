import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        ans=[]

        def originDistance(point):
            x1,y1 = point[0],point[1]
            x2,y2 = 0,0
            return math.sqrt((x1 - x2)**2 +  (y1 - y2)**2)

        for point in points:
            distance = (originDistance(point))
            # print(point)
            # print(distance)
            heapq.heappush(minHeap,[distance,point])
            # heapq.heappush(ansHeap,point)

        for i in range(k):
            pair = heapq.heappop(minHeap)
            ans.append(pair[1])
        return ans

        