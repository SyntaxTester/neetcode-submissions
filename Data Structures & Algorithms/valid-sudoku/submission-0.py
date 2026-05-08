class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        answer = True

        for i in range(len(board)):
            for j in range(len(board)):
                for k in range(len(board)):
                    if board[i][j] == board[i][k] != '.' and j != k:
                        answer = False

        for i in range(len(board)):
            for j in range(len(board)):
                for k in range(len(board)):
                    if board[j][i] == board[k][i] != '.' and j != k:
                        answer = False

        r, c = 0, 0
        b = 0

        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[block_row + i][block_col + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return answer