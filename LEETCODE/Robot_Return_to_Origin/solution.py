from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)
        if counter['U'] == counter['D'] and counter['L'] == counter['R']:
            return True
        return False
