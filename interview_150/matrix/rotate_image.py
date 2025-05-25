class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)

        for i in range(size // 2):
            matrix[i], matrix[size - 1 - i] = matrix[size - 1 - i], matrix[i]

        for x in range(size):
            for y in range(x + 1, size):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        return matrix