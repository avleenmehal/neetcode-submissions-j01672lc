class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateTime(piles, ans):
            sum = 0
            for val in piles:
                sum += math.ceil(val/ans)
            return sum        

        ans = max(piles)
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
