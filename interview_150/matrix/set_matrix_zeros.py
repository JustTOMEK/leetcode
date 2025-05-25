class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_number = len(matrix)
        column_number = len(matrix[0])
        rows = []
        columns = []

        for row in range(row_number):
            for column in range(column_number):
                if matrix[row][column] == 0:
                    rows.append(row)
                    columns.append(column)

        for row in rows:
            for i in range(column_number):
                matrix[row][i] = 0

        for column in columns:
            for i in range(row_number):
                matrix[i][column] = 0
