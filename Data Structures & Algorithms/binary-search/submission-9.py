class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.iterative_bfs(nums, target)
        
    def bfs(self, l: int, r:int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        mid = (l + r)//2 
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.bfs(l,mid-1, nums,target)
        elif nums[mid] < target:
            return self.bfs(mid+1, r,nums, target)


    def iterative_bfs(self, nums: List[int], target: int) -> int:
        l =0
        r= len(nums) - 1

        while l <= r:
            mid = l + ((r-l)//2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid+1
        return -1
