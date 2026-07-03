class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        q = deque([])
        row = len(grid)
        col = len(grid[0])
        minute = 0
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
            
        directions = [[0,1], [1, 0], [-1, 0], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < row and 0 <= newC < col and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        fresh -= 1
            minute += 1
        return minute if fresh == 0 else -1
