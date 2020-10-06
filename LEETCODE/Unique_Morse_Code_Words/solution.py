class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                       "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        unique_transformations = set()

        for word in words:
            converted = [morse_codes[ord(char)-97] for char in word]
            unique_transformations.add("".join(converted))

        return len(unique_transformations)


"""
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                       "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        unique_transformations = set()

        for word in words:
            converted = []
            for char in word:
                converted.append(morse_codes[ord(char)-97])

            unique_transformations.add("".join(converted))

        return len(unique_transformations)
"""
