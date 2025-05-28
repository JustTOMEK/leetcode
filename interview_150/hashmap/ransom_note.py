class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for letter in magazine:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1

        for letter in ransomNote:
            if letter in dict and dict[letter] > 0:
                dict[letter] -= 1
            else:
                return False
        return True