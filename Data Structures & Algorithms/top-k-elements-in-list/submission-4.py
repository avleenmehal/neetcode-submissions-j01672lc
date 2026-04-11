class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        

        return heapq.nlargest(k, count.keys(), key=count.get)

        # newnums = []
        # for key in count:
        #     newnums.append([count[key], key])

        # heapq.heapify(newnums)
        # ans = []
        # while(k):
        #     ans.append(heapq.heappop(newnums)[1])
        #     k -= 1

        # return ans

        