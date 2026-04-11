class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        nums.sort()
        res = set()
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(subset.copy()))
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
            return
        
        dfs(0)
        ans= []
        for l in res:
            ans.append(l)
        return ans
