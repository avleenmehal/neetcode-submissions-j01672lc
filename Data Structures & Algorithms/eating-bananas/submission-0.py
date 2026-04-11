class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        def calculateTime(piles, ans):
            sum = 0
            for val in piles:
                sum += ceil(val/ans)
            
            return sum
        
        if h < len(piles):
            return -1
        
        piles.sort()
        ans = piles[-1]
        time = calculateTime(piles, ans)
        l = 1
        r = ans
        while l<=r:
            mid = ((l+r)//2)
            time = calculateTime(piles, mid)

            if time > h:
                l = mid + 1
            if time <= h:
                ans = mid
                r = mid - 1
        
        return ans
