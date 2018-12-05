class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = 26 * [None]
            self.leaf = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()
    
    def char2ind(self, ch):
        return ord(ch) - ord('a')
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        h.leaf = True
    
    def search_util(self, root, word, level):
        if level == len(word):
            return root.leaf
        
        ch = word[level]
        if ch == '.':
            flag = False
            for i in range(len(root.children)):
                if root.children[i] is not None:
                    nxt = root.children[i]
                    flag = flag or self.search_util(nxt, word, level + 1)
            return flag
        else:
            ind = self.char2ind(ch)
            if root.children[ind] is None:
                return False 
            nxt = root.children[ind]
            return self.search_util(nxt, word, level + 1)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        h = self.root 
        n = len(word)
        if n > 0:
            return self.search_util(h, word, 0)
        return False
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)