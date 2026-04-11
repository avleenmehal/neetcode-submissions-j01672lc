class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda pair: pair[0])
        res=[intervals[0]]
        ans=0
        i = 1
        while i<n:
            if intervals[i][0]>=res[-1][1]:
                res.append(intervals[i])
                i+=1

            elif intervals[i][0]<res[-1][1]:
                
                res[-1][0]=max(res[-1][0],intervals[i][0])
                res[-1][1]=min(res[-1][1],intervals[i][1])
                i+=1
                ans+=1

            elif intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
                i+=1

        return ans