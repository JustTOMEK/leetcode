class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0
        left = 0
        right = 0
        longest_substr = 1
        current_set = set()
        while right < len_s:
            if s[right] in current_set:
                if right - left > longest_substr:
                    longest_substr = right - left
                while s[left] != s[right]:
                    current_set.remove(s[left])
                    left += 1
                current_set.remove(s[left])
                left += 1
            else:
                current_set.add(s[right])
                right += 1
        if right - left > longest_substr:
            longest_substr = right - left
        return longest_substr