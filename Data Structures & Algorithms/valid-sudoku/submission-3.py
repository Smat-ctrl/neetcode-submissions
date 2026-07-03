class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(int)
        columnMap = defaultdict(set)
        threebythree = defaultdict(set)

        for i in range(len(board)):
            rowMap.clear()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                
                # Rows
                if rowMap[board[i][j]] >= 1:
                    return False
                else:
                    rowMap[board[i][j]] += 1
                
                # Columns
                if board[i][j] in columnMap[j]:
                    return False
                else:
                    columnMap[j].add(board[i][j])
                
                # 3x3 Rows
                board_row = i // 3
                board_col = j // 3

                if board[i][j] in threebythree[(board_row, board_col)]:
                    return False
                else:
                    threebythree[(board_row, board_col)].add(board[i][j])
        return True
                