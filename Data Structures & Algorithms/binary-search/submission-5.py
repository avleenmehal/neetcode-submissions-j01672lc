class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bfs(0,len(nums) - 1, nums, target)
        
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
        # else:
        #     return -1