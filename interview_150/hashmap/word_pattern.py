class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_len = len(pattern)
        dictionary = {}

        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(pattern_len):
            if pattern[i] in dictionary:
                if dictionary[pattern[i]] != words[i]:
                    return False
                continue
            elif words[i] in dictionary.values():
                return False
            dictionary[pattern[i]] = words[i]
        return True