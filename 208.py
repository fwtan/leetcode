class Trie:
    class TrieNode:
        def __init__(self):
            self.children = 26 * [None]
            self.val = 0
            self.leaf = False

        def is_leaf(self):
            return self.leaf


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()


    def char2ind(self, ch):
        return ord(ch) - ord('a')


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        n = len(word)
        h = self.root 
        for i in range(n):
            ind = self.char2ind(word[i])
            if h.children[ind] is None:
                h.children[ind] = self.TrieNode()
            h = h.children[ind]
            h.val += 1
        h.leaf = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        h = self.root
        for i in range(n):
            ind = self.char2ind(word[i])
            if h.children[ind] is None:
                return False 
            h = h.children[ind]
        return h.leaf

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        n = len(prefix)
        h = self.root
        for i in range(n):
            ind = self.char2ind(prefix[i])
            if h.children[ind] is None:
                return False 
            h = h.children[ind]
        return h.val > 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)