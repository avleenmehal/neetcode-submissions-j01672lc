class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total%2 != 0:
            return False


        ans = []
        res = []
        def subset(i,currSum):
            if currSum == total/2:
                res.append(ans.copy())
                print("one res is recieved", res)
                return
            if i >=len(nums) or currSum > total/2:            
                return
            print("currsum " , currSum)
            ans.append(nums[i])
            print("ans " , ans)
            subset(i+1,currSum + nums[i])

            ans.pop()
            subset(i+1,currSum)
        subset(0,0)
        print(res)
        # for lis in res:
        #     if sum(lis) == total/2:
        #         c
        if len(res) >=2:
            return True
        return False
        