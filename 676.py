class MagicDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.leaf = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, key):
        n = len(key)
        h = self.root
        for i in range(n):
            ch = key[i]
            if h.children.get(ch, None) is None:
                h.children[ch] = self.TrieNode()
            h = h.children[ch]
        h.leaf = True

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for x in dict:
            self.insert(x)

    def search_util(self, root, word, level, mode):
        if level == len(word):
            if root.leaf and mode:
                return True
            return False
        ch = word[level]
        if mode:
            nxt = root.children.get(ch, None)
            if nxt is None:
                return False 
            return self.search_util(nxt, word, level+1, mode)
        else:
            flag = False
            for x, nxt in root.children.items():
                flag = flag or self.search_util(nxt, word, level+1, not (ch == x))
            return flag

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        n = len(word)
        h = self.root
        return self.search_util(h, word, 0, False)
        

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)