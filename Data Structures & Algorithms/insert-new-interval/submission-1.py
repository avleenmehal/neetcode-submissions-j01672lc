class Solution:
    def insert(self, intervals: List[List[int]], nw: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        res = []
        i = 0
        while i<n and intervals[i][1]<nw[0]:
            res.append(intervals[i])
            print(i)
            i+=1

        while i<n and nw[1]>=intervals[i][0]:
            nw[0] = min(intervals[i][0],nw[0])
            nw[1]=max(intervals[i][1],nw[1])
            print("gerg")
            print(i)
            i+=1
        res.append(nw)
        while i<n and nw[1]<intervals[i][0]:
            res.append(intervals[i])
            i+=1

        return res
            
        