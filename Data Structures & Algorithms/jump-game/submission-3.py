class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        if nums[0] == 0:
            return False
     
        dp = [False] * n
        i=0
        dp[i]=True
        while i <n:
            if dp[i]==False:
                return False
            j = min(i + nums[i],n-1)
            while j<n and j>i:
                dp[j]=True
                j-=1
            i+=1
        return dp[n-1]


        