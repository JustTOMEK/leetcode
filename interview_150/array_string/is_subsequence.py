class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        s_len = len(s)
        s_index = 0
        for letter in t:
            if letter == s[s_index]:
                s_index += 1
            if s_index == s_len:
                return True
        return False