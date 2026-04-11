class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        minHeap = stones
        heapq.heapify(stones)
        print(minHeap)
        while len(minHeap)>1:
            first = -heapq.heappop(minHeap)
            second = -heapq.heappop(minHeap)
            diff = abs(first - second)
            if diff == 0:
                print(minHeap)
                continue
            else: 
                heapq.heappush(minHeap,-diff)
            print(minHeap)
        
        if len(minHeap) == 0:
            return 0
        else:
            return -minHeap[0]

        