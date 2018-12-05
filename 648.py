class Solution:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.children = 26 * [None]
                self.leaf = False
                self.val = None
        
        def __init__(self):
            self.root = self.TrieNode()

        def char2ind(self, ch):
            return ord(ch) - ord('a')
        
        def insert(self, key):
            n = len(key)
            h = self.root 
            for i in range(n):
                ind = self.char2ind(key[i])
                if h.children[ind] is None:
                    h.children[ind] = self.TrieNode()
                elif h.children[ind].leaf:
                    return 
                h = h.children[ind]
            h.leaf = True
            h.val = key

        def search(self, key):
            n = len(key)
            h = self.root 
            for i in range(n):
                ind = self.char2ind(key[i])
                if h.children[ind] is None:
                    return None 
                elif h.children[ind].leaf:
                    return h.children[ind].val 
                h = h.children[ind]
            # if h.leaf:
            #     return h.val 
            return None
                


    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        t = self.Trie()
        for x in dict:
            t.insert(x)
        words = sentence.rstrip().split()
        new_sent = []
        for x in words:
            y = t.search(x)
            if y is not None:
                new_sent.append(y)
            else:
                new_sent.append(x)
        return ' '.join(new_sent)
