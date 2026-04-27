class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            nums[i] = -1*nums[i]

        for i in range(k):
            heapq.heappush(heap,(nums[i],i))
        
        print(heap)
        ans = []
        l =0
        r = k-1
        while(r<len(nums)):
            heapq.heappush(heap, (nums[r],r))
            while heap[0][1]<l:
                heapq.heappop(heap)
            ans.append(-1*heap[0][0])
            r+=1
            l+=1

        return ans
        