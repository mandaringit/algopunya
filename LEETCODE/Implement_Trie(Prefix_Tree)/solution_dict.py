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
        node = self.root
        for i, char in enumerate(word):
            prefix = word[:i + 1]

            if prefix in node:
                node = node[prefix]  # 다음 노드로.
                if prefix == word:
                    node['is_word'] = True  # 만약 단어라면 True 플래그
            else:
                node[prefix] = {'is_word': False}
                node = node[prefix]
                if prefix == word:
                    node['is_word'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i, char in enumerate(word):
            prefix = word[:i + 1]

            if prefix in node:
                node = node[prefix]
                if prefix == word:
                    if node['is_word']:
                        return True
                    return False
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i, char in enumerate(prefix):
            real_prefix = prefix[:i + 1]

            if real_prefix in node:
                node = node[real_prefix]
                if real_prefix == prefix:
                    return True
            else:
                return False


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
