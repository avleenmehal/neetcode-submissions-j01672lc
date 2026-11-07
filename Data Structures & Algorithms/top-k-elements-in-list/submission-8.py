class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        maxHeap = []
        
        for key,val in count.items():
            heapq.heappush(maxHeap, (-1 * val, key))
        res = []
        for _ in range(k):
            res.append(maxHeap[0][1])
            heapq.heappop(maxHeap)

        return res