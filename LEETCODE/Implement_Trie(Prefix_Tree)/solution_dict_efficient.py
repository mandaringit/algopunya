
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {'is_word': False}
            current = current[char]
        current['is_word'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        if current['is_word']:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char in current:
                current = current[char]
            else:
                return False
        return True
