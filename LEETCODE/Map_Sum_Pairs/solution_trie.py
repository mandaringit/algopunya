class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        
        node = self.trie
        for char in key:
            if char not in node:
                node[char] = {'value' : 0}
            node = node[char]
        node['value'] = val

    def sum(self, prefix: str) -> int:
        
        summation = 0
        node = self.trie
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        
        # 해당 노드 포함 모든 자식의 value 더하기.
        stack = [node]
        while stack:
            n = stack.pop()
            
            for key in n:
                if key == 'value':
                    summation += n[key]
                else:
                    stack.append(n[key])
        
        return summation
            
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)