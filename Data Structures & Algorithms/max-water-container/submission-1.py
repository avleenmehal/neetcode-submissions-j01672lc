class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxarea = 0
        while l<r:
            b = r-l
            h = min(heights[l],heights[r])
            maxarea = max(maxarea,b*h)

            if heights[l]<heights[r]:
                l+=1
            # elif heights[l]>heights[r]:
            #     r-=1
            else:
                # l+=1
                r-=1
        return maxarea