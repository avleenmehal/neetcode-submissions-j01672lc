class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        def rob2(nums: List[int]) -> int:
            print(nums)
            if not nums:
                return 0
            dp = [0] * len(nums)
            dp[0]=nums[0]
            if(len(nums)<=2):
                return max(nums)
            dp[1]=max(dp[0],nums[1])
            # print(dp)
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            # print(dp)
            return dp[len(nums)-1]
        
        return max(rob2(nums[0:-1]), rob2(nums[1:]))