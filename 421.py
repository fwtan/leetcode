class Solution:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.children = 2 * [None]
                self.val = -1

        def __init__(self, l):
            self.root = self.TrieNode()
            self.l = l
        
        def int2binary(self, i):
            s = '{:b}'.format(i)
            s = '0' * (self.l - len(s)) + s 
            return s
        
        def binary2int(self, s):
            return int(s, 2)
        
        def insert(self, x):
            key = self.int2binary(x)
            n = len(key)
            h = self.root 
            for i in range(n):
                ind = int(key[i])
                if h.children[ind] is None:
                    h.children[ind] = self.TrieNode()
                h = h.children[ind]
            h.val = x 
            
        def max_bit_diff_xor(self, x):
            key = self.int2binary(x)
            n = len(key)
            h = self.root
            for i in range(n):
                ind = int(key[i])
                if h.children[1-ind] is not None:
                    h = h.children[1-ind]
                elif h.children[ind] is not None:
                    h = h.children[ind]
            return x^h.val
    
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_int = -1
        for i in range(0, len(nums)):
            max_int = max(max_int, nums[i])
        l = len('{:b}'.format(max_int))

        t = self.Trie(l)
        t.insert(nums[0])
        max_xor = 0
        for i in range(1, len(nums)):
            cur_xor = t.max_bit_diff_xor(nums[i])
            max_xor = max(cur_xor, max_xor)
            t.insert(nums[i])
        return max_xor
        