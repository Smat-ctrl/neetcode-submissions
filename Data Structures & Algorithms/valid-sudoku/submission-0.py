class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashMap = defaultdict(set)
        columnMap = defaultdict(set)
        threeBythree = defaultdict(set)
        
        for i in range(len(board)):

            # Rows
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in hashMap[i]:
                    return False
                hashMap[i].add(board[i][j])
            
            # Columns
                if board[i][j] in columnMap[j]:
                    return False
                columnMap[j].add(board[i][j])
            
            # 3 x 3
                box_number_row = i // 3
                box_number_col = j // 3

                if board[i][j] in threeBythree[(box_number_row, box_number_col)]:
                    return False
                else:
                    threeBythree[(box_number_row, box_number_col)].add(board[i][j])        
        
        return True


