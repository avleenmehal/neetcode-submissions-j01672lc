class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols= len(grid[0])
        drcn = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()

        def checkT(i,j):
            for dr,dc in drcn:
                if i+dr>=0 and j+dc>=0 and i+dr<rows and j+dc<cols and grid[i+dr][j+dc]==2147483647:
                    grid[i+dr][j+dc]=min(grid[i+dr][j+dc], grid[i][j] + 1)
                    queue.append((i+dr,j+dc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        print(queue)

        while queue:
            i,j=queue.popleft()
            checkT(i,j)

        # return grid



        