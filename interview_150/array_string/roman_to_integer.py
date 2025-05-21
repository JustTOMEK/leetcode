class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        last_one = s[0]
        number = 0

        for letter in s:
            if dictionary[last_one] < dictionary[letter]:
                number += dictionary[letter] - 2 * dictionary[last_one]
            else:
                number += dictionary[letter]
            last_one = letter
        return number