class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        

        def dfs(vis, per):
            if False not in vis:
                res.append(per.copy())
                return
            for j in range(len(nums)):
                if vis[j]==False:
                    per.append(nums[j])
                    vis[j] = True
                    dfs(vis,per)
                    vis[j]=False
                    per.pop()


        # for i in range(len(nums)):
        #     per = []
        #     per.append(nums[i])
        vis =[False] * len(nums)
        #     vis[i] = True
        dfs(vis, [])

    
        return res