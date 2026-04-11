class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        def child(r,c):

            for dr, dc in direction:
                nr,nc = r+dr , c+dc

                if nr>=0 and nc>=0 and nr<rows and nc<cols and grid[nr][nc]==1:
                    queue.append((nr,nc))
                    grid[nr][nc]=-1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area = 0
                    queue.append((r,c))
                    grid[r][c] = -1

                    while queue:
                        area+=1
                        rq,cq = queue.popleft()
                        child(rq,cq)

                    res = max(area,res)


        return res