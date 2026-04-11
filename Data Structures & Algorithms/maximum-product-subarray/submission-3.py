class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            tmp2 = curMin * num
            curMax = max(tmp, tmp2, num)
            curMin = min(tmp, tmp2, num)
            res = max(res, curMax)
        return res