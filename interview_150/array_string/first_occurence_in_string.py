class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            print(haystack[i:i + needle_len])
            if haystack[i:i + needle_len] == needle:
                return i
        return -1