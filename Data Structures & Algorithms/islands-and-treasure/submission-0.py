from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        resGrid = []
        copyMatrix = []
        idxOfLand = []
        land = 2**31 - 1
        treasure = 0
        water = -1

        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                if grid[i][j] == land:
                    idxOfLand.append((i, j))
                row.append(grid[i][j])
            copyMatrix.append(row)

        q = deque()
        for i in range(len(copyMatrix)):
            for j in range(len(copyMatrix[0])):
                if copyMatrix[i][j] == treasure:
                    q.append((i, j))

        def bfs():
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if not (0 <= newRow < len(copyMatrix) and 0 <= newCol < len(copyMatrix[0])):
                        continue
                    if copyMatrix[newRow][newCol] == water or copyMatrix[newRow][newCol] == treasure:
                        continue
                    if copyMatrix[newRow][newCol] != land:
                        continue

                    copyMatrix[newRow][newCol] = copyMatrix[row][col] + 1
                    q.append((newRow, newCol))

        bfs()

        for i, j in idxOfLand:
            grid[i][j] = copyMatrix[i][j]