class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        for word in strs:
            chars = [0]*26

            for char in word:
                idx = ord(char) - 97
                chars[idx] += 1

            key = tuple(chars)
            if key in counter:
                counter[key].append(word)
            else:
                counter[key] = [word]

        return counter.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in counter:
                counter[key].append(word)
            else:
                counter[key] = [word]

        return counter.values()
