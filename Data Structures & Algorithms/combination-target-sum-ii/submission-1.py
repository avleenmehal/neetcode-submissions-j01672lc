class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        subset=[]
        nums.sort()

        res = []

        def dfs(i, target):

            if i>len(nums) or target<0:
                return
            if i ==len(nums):
                if target == 0:
                    res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1,target-nums[i])

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            subset.pop()
            dfs(i+1,target)

        dfs(0,target)

        return res

