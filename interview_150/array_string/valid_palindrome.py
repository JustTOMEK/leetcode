class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_String = ""
        for letter in s:
            if letter.isalnum():
                new_String += letter.lower()
        return new_String[::-1] == new_String