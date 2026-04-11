class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        prod = 1
        for i in nums:
            if i==0:
                count+=1
            else:
                prod *= i

        if count>1:
            ans =[0]*len(nums)
            return ans
        elif count == 1:
            print(prod)
            ans = []
            for num in nums:
                if num == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
            return ans
        else:
            ans = []
            for num in nums:
                ans.append(prod//num)
            return ans
                
