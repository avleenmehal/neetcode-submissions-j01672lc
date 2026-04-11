class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = m + n - 2
        ans = math.comb(steps,m-1)
        return ans
        