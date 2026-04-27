class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k-1):
            heapq.heappush(heap,(-nums[i],i))
        
        ans = []
        l = 0
        r = k-1
        while(r<len(nums)):
            heapq.heappush(heap, (-nums[r],r))
            while heap[0][1]<l:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            r+=1
            l+=1

        return ans
        