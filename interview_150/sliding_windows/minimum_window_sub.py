class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        len_t = len(t)
        output = len_s + 1
        output_str = ""
        left = 0
        right = 0

        t_dict = {}
        current_dict = {}
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                current_dict[letter] = 0
                t_dict[letter] = 1

        right_numbers = 0
        while right < len_s:
            if s[right] in t_dict:
                if current_dict[s[right]] >= t_dict[s[right]]:
                    current_dict[s[right]] += 1
                else:
                    right_numbers += 1
                    current_dict[s[right]] += 1
            if right_numbers == len_t:
                while True:
                    if s[left] in current_dict:
                        if current_dict[s[left]] == t_dict[s[left]]:
                            break
                        else:
                            current_dict[s[left]] -= 1
                    left += 1
                if right - left < output:
                    output = right - left
                    output_str = s[left:right + 1]
            right += 1

        if output == (len_s + 1):
            return ""
        else:
            return output_str
