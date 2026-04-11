class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(i, sum):
            if i==n:
                return sum == target
            # if i == n and sum == target:
            #     return 1
            
            return dfs(i+1,sum+nums[i]) + dfs(i+1,sum-nums[i])
        return dfs(0,0)    
            
        