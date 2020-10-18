class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        pairs = set()
        for S in A:
            odd = tuple(sorted(S[1::2]))
            even = tuple(sorted(S[::2]))
            pairs.add((odd,even))
        
        return len(pairs)
            