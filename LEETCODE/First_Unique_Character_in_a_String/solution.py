class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters = {}
    
        for i, char in enumerate(s):
            if char in characters:
                characters[char][0] = True
            else:
                characters[char] = [False, i]
        
        for char in characters:
            if not characters[char][0]:
                return characters[char][1]
        
        return -1
        