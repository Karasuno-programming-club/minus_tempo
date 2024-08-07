class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sc = [*reversed(sorted(citations))]
        for i in range(len(citations)):
            if sc[i] <= i+1:
                return max(i,sc[i])
        return len(citations)
