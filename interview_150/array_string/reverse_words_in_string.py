class Solution:
    def reverseWords(self, s: str) -> str:
        s_reversed = ""
        for word in s.split()[::-1]:
            s_reversed += word + " "
        s_reversed.strip()
        return s_reversed[:-1]
