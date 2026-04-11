class Solution:
    def solve(self, board: List[List[str]]) -> None:

        drcn = [(1,0),(-1,0),(0,1),(0,-1)]

        def checkT():
            queue = deque()
            for i in range(rows):
                for j in range(cols):
                    if i ==0 or j ==0 or i==rows-1 or j ==cols-1 and board[i][j] == "O":
                        queue.append((i,j))

            while queue:
                r,c = queue.popleft()
                if board[r][c] == "O":
                    board[r][c] = "V"
                    for dr,dc in drcn:
                        if r+dr>=0 and c+dc>=0 and r+dr<rows and c+dc<cols:
                            queue.append((r+dr,c+dc))


        
        rows = len(board)
        cols = len(board[0])
        checkT()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "V":
                    board[i][j] = "O"
        
        return
        