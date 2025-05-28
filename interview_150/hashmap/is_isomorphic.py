class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        str_len = len(s)
        dictionary = {}

        for i in range(str_len):
            if s[i] in dictionary:
                if dictionary[s[i]] != t[i]:
                    return False
                continue
            elif t[i] in dictionary.values():
                return False
            dictionary[s[i]] = t[i]
        return True