class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        stack = deque()
        rows = len(grid)
        col = len(grid[0])
        
        dirc = [[0,-1],[0,1],[1,0],[-1,0]]
        
        def child(i,j):
            clist =[]
            for d in dirc:
                if i+d[0]<rows and j+d[1]<col and i+d[0]>=0 and j+d[1]>=0 and grid[i+d[0]][j+d[1]] == "1":
                    clist.append([i+d[0],j+d[1]])
            print("clistbelow")
            print(clist)
            return clist

        for i in range(rows):
            for j in range(col):
                if grid[i][j] == "1":
                    stack.append([i,j])
                    # print(grid[i][j])
                    # print(stack)
                    while stack:
                        r,c = stack.popleft()
                        # r,c = node[0],node[1]
                        landContinue = child(r,c)
                        print(landContinue)
                        for lc in landContinue:
                            stack.append(lc)

                        grid[r][c] = "-1"
                        print(grid)
                    islands+=1

        return islands