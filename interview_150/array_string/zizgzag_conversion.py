class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for i in range(numRows)]


        phase = "down"
        row_number = 0

        for char in s:
            rows[row_number].append(char)
            if row_number == 0:
                phase = "down"
            elif row_number == numRows - 1:
                phase = "up"
            if phase == "up":
                row_number -= 1
            else:
                row_number += 1

        answer = ""
        for row in rows:
            for letter in row:
                answer += letter
        return answer
