class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        left = [0] * len(height)
        right = [0] * len(height)
        n = len(height) - 1
        left[0] = height[0]
        right[n] = height[n]
        for i in range(1,n+1):
            left[i] = max(left[i-1],height[i])
            right[n-i] = max(right[n-i+1],height[n-i])

        for i in range(n+1):
            if left[i]>height[i] and right[i]>height[i]:
                ans += min(left[i],right[i]) - height[i]

        return ans