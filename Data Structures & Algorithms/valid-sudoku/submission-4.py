class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxMap = defaultdict(set)

        for i in range(len(board)):

            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                if board[i][j] in rowMap[i]:
                    return False
                else:
                    rowMap[i].add(board[i][j])
                
                if board[i][j] in colMap[j]:
                    return False
                else:
                    colMap[j].add(board[i][j])
                
                box_col = j // 3
                box_row = i // 3

                if board[i][j] in boxMap[(box_row, box_col)]:
                    return False
                else:
                    boxMap[(box_row, box_col)].add(board[i][j])
        return True