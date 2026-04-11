class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 1
        numSet = set(nums)
        maxlength,length = 0,0
        for value in numSet:
            if (value - 1) in numSet:
                length = 0
                continue
            else:
                while((value + length) in numSet):
                    length += 1
                    maxlength= max(length,maxlength)

        return maxlength
        