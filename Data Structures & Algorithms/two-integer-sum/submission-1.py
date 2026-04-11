class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in mp:
                return [mp[complement], i]
            mp[num] = i