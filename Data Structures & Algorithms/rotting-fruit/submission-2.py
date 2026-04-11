class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = 0
        rows = len(grid)
        col = len(grid[0])

        def convertRotten(i,j,fresh):
            if i-1 >= 0 and grid[i-1][j] == 1:
                fresh-=1
                grid[i-1][j] = 2
                rotList.append([i-1,j])
            if i+1 < rows and grid[i+1][j] == 1:
                fresh-=1
                grid[i+1][j] = 2
                rotList.append([i+1,j])
            if j-1 >= 0 and grid[i][j-1] == 1:
                fresh-=1
                grid[i][j-1] = 2
                rotList.append([i,j-1])
            if j+1 < col and grid[i][j+1] == 1:
                fresh-=1
                grid[i][j+1] = 2
                rotList.append([i,j+1])
            print("Inside convert method")
            print(len(rotList))
            return fresh

        rotList = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    rotList.append([i,j])
                    rotten +=1

        if fresh == 0:
            return 0
        print(rotList)
        # node = rotList.popleft()
        mins = 0
        while rotList:
            l = len(rotList)
            print(rotList)
            for i in range(l):
                node = rotList.popleft()
                fresh = convertRotten(node[0],node[1],fresh)
                i+=1
            mins +=1
            if fresh == 0:
                return mins

        return mins if fresh == 0 else -1
                        
                    
