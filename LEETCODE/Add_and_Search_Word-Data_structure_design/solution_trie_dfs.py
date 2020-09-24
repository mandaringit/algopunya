class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for char in word:
            if char not in node:
                node[char] = {'is_word': False}
            node = node[char]

        node['is_word'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self.trie, 0)]  # 현시점 검색해야할 노드들

        while stack:
            node, idx = stack.pop()
            if idx == len(word):
                if node['is_word']:
                    return True
            else:
                char = word[idx]
                if char == '.':
                    for key in node:
                        if key != 'is_word':
                            stack.append((node[key], idx + 1))
                else:
                    if char in node:
                        stack.append((node[char], idx + 1))

        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
obj.addWord("pad")
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
print(obj.search("b..."))
print(obj.search("b."))
# param_2 = obj.search(word)
