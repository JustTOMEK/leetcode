class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maks = ""
        for i in range(1, len(strs[0]) + 1):
            check = strs[0][:i]
            for j in range(len(strs)):
                if strs[j].startswith(strs[0][:i]):
                    maks = strs[0][:i]
                else:
                    maks = strs[0][:i - 1]
                    break
            if len(maks) != i:
                break
        return maks
