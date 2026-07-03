class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        rows = len(board)
        cols = len(board[0])

        def bfs(r, c, visit):
            if (r,c) in visit:
                return
            visit.add((r,c))
            q = deque([(r,c)])
            directions = [[0,1], [1,0], [-1, 0], [0, -1]]
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        newRow, newCol = row + dr, col + dc
                        if 0 <= newRow < rows and 0 <= newCol < cols and board[newRow][newCol] == 'O' and (newRow, newCol) not in visit:
                            visit.add((newRow, newCol))
                            q.append((newRow, newCol))
                
        for col in range(cols):
            if board[0][col] == 'O':
                bfs(0, col, visit)
            if board[rows - 1][col] == 'O':
                bfs(rows - 1, col, visit)
        
        for r in range(rows):
            if board[r][0] == 'O':
                bfs(r, 0, visit)
            if board[r][cols - 1] == 'O':
                bfs(r, cols - 1, visit)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in visit:
                    board[i][j] = 'X'
        