class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = [[]]

        # for num in nums:
        #     res += [subset + [num] for subset in res]

        # return res

        subset = []
        res = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
            return
        
        dfs(0)
        return res
