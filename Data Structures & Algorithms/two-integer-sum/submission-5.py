class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i,n in enumerate(nums):
            mapp[n] = i

        for i,n in enumerate(nums):
            if (target - n) in mapp and mapp[target - n] != i:
                ans = []
                ans.append(i)
                ans.append(mapp[target - n])
                return sorted(ans)
            