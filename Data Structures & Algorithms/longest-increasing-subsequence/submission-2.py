class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i],1+lis[j])
        print(lis)
        return max(lis)
        