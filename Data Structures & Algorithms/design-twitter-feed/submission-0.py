class Twitter:
    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append((self.count,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # heap = []
        # # USERS ki khudki posts heap me add
        # for pari in self.tweetMap[userId]:
        #     heap.append(pari)
        # heapq.heapify(heap) # Sorted them on timestamp

        # # Ab daalenge Users k followers k tweets
        # for followee in self.followMap[userId]:
        #     for pari in self.tweetMap[followee]:
        #         heapq.heappush(heap,pari)
        #         
        # # heapq.heapify(heap)
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
