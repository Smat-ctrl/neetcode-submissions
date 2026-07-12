class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxMap = defaultdict(set)
        colMap = defaultdict(set)
        for i in range(len(board)):
            rowMap = defaultdict(int)
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in rowMap:
                    return False
                else:
                    rowMap[board[i][j]] += 1
                
                if board[i][j] in colMap[j]:
                    return False
                else:
                    colMap[j].add(board[i][j])
                
                box = (i // 3, j // 3)

                if board[i][j] in boxMap[box]:
                    return False
                else:
                    boxMap[box].add(board[i][j])
        
        return True
                
                


