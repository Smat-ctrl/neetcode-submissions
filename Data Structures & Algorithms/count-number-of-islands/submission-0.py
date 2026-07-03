from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visit = set()
        islands = 0

        def bfs(r, c):
            q = deque([(r, c)])
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    if (
                        0 <= newRow < len(grid)
                        and 0 <= newCol < len(grid[0])
                        and grid[newRow][newCol] == "1"
                        and (newRow, newCol) not in visit
                    ):
                        visit.add((newRow, newCol))
                        q.append((newRow, newCol))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    visit.add((i, j))
                    bfs(i, j)
                    islands += 1

        return islands