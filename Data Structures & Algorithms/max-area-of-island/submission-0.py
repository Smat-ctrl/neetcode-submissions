class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        self.maxArea = 0
        visit = set(())

        def bfs(r, c):

            q = deque([(r,c)])
            directions = [[0,1], [1,0], [-1, 0], [0, -1]]
            numberOfLand = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if (
                        0 <= newRow < len(grid)
                        and 0 <= newCol < len(grid[0])
                        and grid[newRow][newCol] == 1
                        and (newRow, newCol) not in visit
                        ):
                        visit.add((newRow, newCol))
                        q.append((newRow, newCol))
                        numberOfLand += 1
            self.maxArea = max(self.maxArea, numberOfLand)
                    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i ,j) not in visit and grid[i][j] == 1:
                    visit.add((i,j))
                    bfs(i,j)
        
        return self.maxArea
