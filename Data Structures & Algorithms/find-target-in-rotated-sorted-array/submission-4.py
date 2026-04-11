class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binarySearch(left, right):
            while left<=right:
                mid = (left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
            return -1

        result = binarySearch(0,pivot-1)
        if result is not -1:
            return result
        
        return binarySearch(pivot,len(nums)-1)
        