class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))
#         words = s.split(" ")

#         reversed_words = []
#         for word in words:
#             chars = list(word)
#             l,r = 0, len(chars) - 1

#             while l < r:
#                 chars[l], chars[r] = chars[r], chars[l] # swap
#                 l += 1
#                 r -= 1

#             reversed_words.append("".join(chars))

#         return " ".join(reversed_words)
