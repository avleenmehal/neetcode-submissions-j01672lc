class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp =[[[1,1]] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = (nums[i],nums[i])

        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                left = dp[i][j-1]
                down = dp[i+1][j]
                diag = dp[i+1][j-1]
                if diag[1] == 0:
                    prod = 0
                else:
                    prod = (left[1]*down[1])//diag[1]
                dp[i][j]=[max(left[0],down[0],prod),prod]
        print(dp)
        ans = dp[0][n-1]
        return ans[0]
        
            
        
            


        