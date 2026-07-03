class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        q = deque(())
        rows = len(grid)
        cols = len(grid[0])
        land = 2**31 - 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            directions = [[0,1],[1,0], [-1,0],[0,-1]]
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == land:
                        grid[newR][newC] = grid[r][c] + 1
                        q.append((newR, newC))
        