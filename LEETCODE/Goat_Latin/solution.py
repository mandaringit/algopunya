class Solution:
    def toGoatLatin(self, S: str) -> str:

        words = S.split(" ")
        vowel = 'aeiouAEIOU'
        for i, word in enumerate(words):
            if word[0] not in vowel:
                words[i] = word[1:] + word[0]
            words[i] = words[i] + 'ma' + 'a' * (i+1)

        return ' '.join(words)
