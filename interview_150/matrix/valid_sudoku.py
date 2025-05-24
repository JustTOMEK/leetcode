def check_rows(board):
    for row in board:
        numbers = []
        for number in row:
            if number.isnumeric():
                if 0 < int(number) < 10 and number not in numbers:
                    numbers.append(number)
                else:
                    return False
    return True

def check_columns(board):
    for i in range(0, 9):
        numbers = []
        for j in range(0, 9):
            number = board[j][i]
            if number.isnumeric():
                if 0 < int(number) < 10 and number not in numbers:
                    numbers.append(number)
                else:
                    return False
    return True

def check_sub_boxes(board):
    for i in range(0, 3):
        for j in range(0, 3):
            numbers = []
            for k in range(0, 3):
                for l in range(0, 3):
                    number = board[i*3 + k][j*3 + l]
                    if number.isnumeric():
                        if 0 < int(number) < 10 and number not in numbers:
                            numbers.append(number)
                        else:
                            return False
    return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return check_rows(board) and check_columns(board) and check_sub_boxes(board)