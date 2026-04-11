class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        drc = [(0,1),(1,0),(-1,0),(0,-1)]

        setPacific = set()
        setAtlantic = set()

        def dfs(i,j,visited, prevHeight):
            if ((i,j) in visited or i < 0 or j<0 or i==rows or j==cols or heights[i][j] < prevHeight):
                return
            visited.add((i,j))
            for dr,dc in drc:
                dfs(i+dr,j+dc,visited,heights[i][j])



        for i in range(rows):
            dfs(i,0,setPacific, heights[i][0])
        for j in range(cols):
            dfs(0,j,setPacific, heights[0][j])
        for i in range(rows):
            dfs(i,cols-1,setAtlantic, heights[i][cols-1])
        for j in range(cols):
            dfs(rows-1,j,setAtlantic, heights[rows-1][j])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in setPacific and (r, c) in setAtlantic:
                    res.append([r, c])
        return res
        
        