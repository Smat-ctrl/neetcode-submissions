class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colMap = {}
        dimensionMap = {}

        for i in range(len(board)):
            rowMap = defaultdict(int)
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] not in rowMap:
                    rowMap[board[i][j]] += 1
                else:
                    return False
                
                if board[i][j] in colMap and colMap[board[i][j]] == j:
                    return False
                else:
                    colMap[board[i][j]] = j
                
                dimJ = j // 3
                dimR = i // 3

                if board[i][j] in dimensionMap and dimensionMap[board[i][j]] == (dimR, dimJ):
                    return False
                else:
                    dimensionMap[board[i][j]] = (dimR, dimJ)
        
        return True


