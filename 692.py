class Solution:
    class heap:
        class heap_node:
            def __init__(self, freq, word):
                self.freq = freq
                self.word = word
        
        def __init__(self, k):
            self.nodes = []
            self.word2ind = {}
            self.hsize = 0
            self.k = k
            
        def compare(self, i1, i2):
            if self.nodes[i1].freq < self.nodes[i2].freq:
                return True 
            elif self.nodes[i1].freq == self.nodes[i2].freq:
                return self.nodes[i1].word > self.nodes[i2].word
            return False

        def swap_node(self, i1, i2):
            self.word2ind[self.nodes[i1].word] = i2
            self.word2ind[self.nodes[i2].word] = i1

            tmp = self.nodes[i1]
            self.nodes[i1] = self.nodes[i2]
            self.nodes[i2] = tmp 
   
        def heapify(self, i):
            s = i 
            l = 2*i+1
            r = 2*i+2
            if l < self.hsize and self.compare(l, s):
                s = l 
            if r < self.hsize and self.compare(r, s):
                s = r 
            if s != i:
                self.swap_node(i, s)
                self.heapify(s)

        def update(self, i):
            s = i 
            p = (s-1)//2
            if p >= 0:
                if self.compare(s, p):
                    self.swap_node(s, p)
                    self.update(p)
        
        def insert(self, word, count):
            node = self.heap_node(count, word)
            if self.hsize < self.k:
                self.nodes.append(node)
                self.hsize += 1
                self.word2ind[word] = self.hsize-1
                self.update(self.hsize-1)
            elif (count > self.nodes[0].freq) or (count == self.nodes[0].freq and word < self.nodes[0].word):
                self.nodes[0] = node 
                self.word2ind[word]=0
                self.heapify(0)
        
        def extract_min(self):
            if self.hsize > 0:
                mword = self.nodes[0].word
                self.swap_node(0, self.hsize-1)
                self.hsize -= 1
                self.heapify(0)
                return mword
            return None


    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word2freq = {}
        for x in words:
            if word2freq.get(x, None) is None:
                word2freq[x] = 1
            else:
                word2freq[x] += 1
        h = self.heap(k)
        for w, c in word2freq.items():
            h.insert(w, c)
        res = []
        for i in range(k):
            w = h.extract_min()
            res.append(w)
        return res[::-1]
            