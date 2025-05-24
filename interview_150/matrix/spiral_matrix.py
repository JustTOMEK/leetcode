class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x, y = 0, 0
        phase = "right"
        top_border = 0
        bottom_border = len(matrix)
        left_border = 0
        right_border = len(matrix[0])
        output = []
        while True:
            if phase == "right":
                if x == right_border - 1:
                    phase = "down"
                    top_border += 1
                else:
                    output.append(matrix[y][x])
                    x += 1
            elif phase == "down":
                if y == bottom_border - 1:
                    phase = "left"
                    right_border -= 1
                else:
                    output.append(matrix[y][x])
                    y += 1
            elif phase == "left":
                if x == left_border:
                    phase = "up"
                    bottom_border -= 1
                else:
                    output.append(matrix[y][x])
                    x -= 1
            else:
                if y == top_border:
                    phase = "right"
                    left_border += 1
                else:
                    output.append(matrix[y][x])
                    y -= 1
            if bottom_border == top_border or left_border == right_border:
                output.append(matrix[y][x])
                break

        return output

