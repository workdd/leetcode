class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "#" in node
            ch = word[i]
            if ch == ".":
                for child in node:
                    if child != "#" and dfs(node[child], i + 1):
                        return True
            if ch not in node:
                return False
            return dfs(node[ch], i + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
