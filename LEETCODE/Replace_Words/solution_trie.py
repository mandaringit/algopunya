class Trie:

    def __init__(self):
        self.root = {}

    def insertion(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {'is_word': False}
            node = node[char]
        node['is_word'] = True

    def replace_successor(self, word):
        node = self.root
        prefix = []
        for char in word:
            if char not in node:
                return word
            node = node[char]
            prefix.append(char)

            if node['is_word']:
                return ''.join(prefix)

        return ''.join(prefix)


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insertion(word)

        words = sentence.split(" ")
        replaced_words = []
        for i, word in enumerate(words):
            new_word = trie.replace_successor(word)
            replaced_words.append(new_word)

        return " ".join(replaced_words)
