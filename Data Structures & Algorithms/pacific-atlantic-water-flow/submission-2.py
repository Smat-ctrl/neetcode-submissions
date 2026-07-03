class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows = len(heights)
        cols = len(heights[0])

        def bfs(r, c, visit):
            if (r, c) in visit:
                return
    
            visit.add((r, c))
            q = deque([(r, c)])
            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            while q:
                row, col = q.popleft()
                lastHeight = heights[row][col]

                for dr, dc in directions:
                    newR, newC = row + dr, col + dc
                    if (
                        0 <= newR < rows and
                        0 <= newC < cols and
                        (newR, newC) not in visit and
                        heights[newR][newC] >= lastHeight
                        ):
                        visit.add((newR, newC))
                        q.append((newR, newC))



        for i in range(rows):
            bfs(i, 0, pac)
            bfs(i, cols - 1, atl)
        
        for i in range(cols):
            bfs(0, i, pac)
            bfs(rows - 1, i, atl)

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i,j])
        
        return res

    




        
