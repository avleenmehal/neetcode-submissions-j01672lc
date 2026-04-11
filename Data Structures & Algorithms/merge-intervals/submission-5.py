class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if len(intervals) <= 1:
            return intervals
        
        i = 1
        intervals.sort(key=lambda pair: pair[0])

        print(intervals)
        res=[intervals[0]]

        while i<n:
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
                i+=1

            elif intervals[i][0]<=res[-1][1]:
                res[-1][0]=min(res[-1][0],intervals[i][0])
                res[-1][1]=max(res[-1][1],intervals[i][1])
                i+=1

        # res.append(intervals[i])

            elif intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
                i+=1

        
        # res.append(intervals[j])
        return res



        