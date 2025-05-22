class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i, citation in enumerate(citations):
            if n - i <= citation:
                return n - i
        return 0

