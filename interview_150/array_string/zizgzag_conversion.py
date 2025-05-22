class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = []
        for i in range(numRows):
            rows.append([])
            for j in range(len(s)):
                rows[i].append('')


        char_index = 0
        rows[0][0] = s[char_index]
        phase = 'down'
        x = 0
        y = 0
        while char_index < len(s) - 1:
            char_index += 1
            if y == 0:
                phase = 'down'
            elif y == numRows - 1:
                phase = 'up'
            if phase == 'up':
                x += 1
                y -= 1
            else:
                y += 1
            rows[y][x] = s[char_index]

        answer = ''
        for row in rows:
            for letter in row:
                answer += letter

        return answer