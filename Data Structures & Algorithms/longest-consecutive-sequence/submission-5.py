class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlength = 0
        length = 0 

        arr = set(nums)

        for num in arr:
            if (num - 1) in arr:
                length = 0 
                continue
            else:
                while (num+length) in arr:
                    length+=1
                    maxlength = max(maxlength, length)
        return maxlength
        