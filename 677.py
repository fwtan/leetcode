class MapSum:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.leaf = False
            self.val = 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        n = len(key)
        h = self.root 
        for i in range(n):
            ch = key[i]
            if h.children.get(ch, None) is None:
                h.children[ch] = self.TrieNode()
            h = h.children[ch]
        h.leaf = True
        h.val = val

    
    def sum_util(self, root):
        val = 0
        if root.leaf:
            val += root.val 
        if len(root.children) > 0:
            for ch, nxt in root.children.items():
                val += self.sum_util(nxt)
        return val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        n = len(prefix)
        h = self.root 
        for i in range(n):
            ch = prefix[i]
            if h.children.get(ch, None) is None:
                return 0
            h = h.children[ch]
        return self.sum_util(h)

        
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)