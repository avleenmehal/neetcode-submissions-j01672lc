class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for u,v,t in times:
            adj[u].append((v,t))

        visited = set()

        minheap = []
        heapq.heappush(minheap, (0,k))
        t = 0
        while minheap:
            w1,n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = w1
            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap,(w1+w2,n2))
        
        if len(visited) == n:
            return t
        return -1
        