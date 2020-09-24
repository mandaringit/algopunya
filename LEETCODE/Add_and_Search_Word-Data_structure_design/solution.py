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
        current_nodes = [self.trie]  # 현시점 검색해야할 노드들
        for char in word:
            next_nodes = []  # 다음에 검색해야할 노드를 쌓는다.
            while current_nodes:
                node = current_nodes.pop()
                if char == '.':
                    for key in node:
                        if key != 'is_word':
                            next_nodes.append(node[key])
                else:
                    if char in node:
                        next_nodes.append(node[char])

            if not next_nodes:  # 더 진행해야하는데 자식 노드들이 없다? 그렇다면 검색 실패.
                return False

            current_nodes = next_nodes  # 다음에 검색할 노드로 교체하기.

        # 결과적으로 모양과 길이는 만족하는 노드들이 남음
        for node in current_nodes:
            if node['is_word']:  # 마지막으로 해당 노드들이 단어에 해당하는게 있는지 확인
                return True
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
