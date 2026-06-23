class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in r[row] or 
                    board[row][col] in c[col] or 
                    board[row][col] in square[(row//3, col//3)]):
                    return False
                
                c[col].add(board[row][col])
                r[row].add(board[row][col])
                square[(row//3, col//3)].add(board[row][col])

        return True        
