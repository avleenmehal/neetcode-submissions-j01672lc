class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] -= 1
        
        newnums = []
        for key in count:
            newnums.append([count[key], key])
        
        ans = heapq.nsmallest(k,newnums)
        print(ans)
        res = []
        for item in ans:
            res.append(item[1])
        return res
        # heapq.heapify(newnums)
        # ans = []
        # while(k):
        #     ans.append(heapq.heappop(newnums)[1])
        #     k -= 1

        return ans

        