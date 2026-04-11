class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = collections.defaultdict(List)

        def calcDist(x,y,x1,y1):
            return abs(x-x1) + abs(y-y1)

        for i in range(len(points)):
            x,y = points[i]
            adj[(x,y)] = []
        for i in range(len(points)):
            x,y = points[i]
            for j in range(len(points)):
                x1,y1 = points[j]
                if x1==x and y1==y:
                    continue
                dist = calcDist(x,y,x1,y1)
                adj[(x,y)].append((dist,(x1,y1)))

        minHeap = []
        heapq.heappush(minHeap, (0,(points[i][0],points[i][1])))
        cost = 0

        visited = set()
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if (n1[0],n1[1]) in visited:
                continue
            cost += w1
            visited.add(n1)
            for w2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w2,n2))
        return cost
