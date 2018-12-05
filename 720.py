class Solution:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.children = 26 * [None]
                self.leaf = False 

        def __init__(self):
            self.root = self.TrieNode()
        
        def char2ind(self, ch):
            return ord(ch) - ord('a')

        def insert(self, key):
            n = len(key)
            h = self.root 
            flag = True
            for i in range(n):
                ind = self.char2ind(key[i])
                if h.children[ind] is None:
                    h.children[ind] = self.TrieNode()
                h = h.children[ind]
                if i < n-1 and h.leaf == False:
                    flag = False
            h.leaf = True
            return flag

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        t = self.Trie()
        words = sorted(words)
        candidates = []
        l = -1
        for i in range(len(words)):
            key = words[i]
            if t.insert(key):
                cur_l = len(key)
                if cur_l > l:
                    candidates = [key]
                    l = cur_l
                elif cur_l == l:
                    candidates.append(key)
        if len(candidates) == 0:
            return ''
        elif len(candidates) == 1:
            return candidates[0]
        else:
            candidates = sorted(candidates)
            return candidates[0]
