class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(currSum, i):
            if currSum == target:
                res.append(subset.copy())
                return
                
            if i>=len(nums) or currSum > target:
                return

            currSum += nums[i]

            subset.append(nums[i])
            
            
            
            dfs(currSum, i)
            subset.pop()
            dfs(currSum - nums[i], i+1)

        dfs(0,0)
        return res

