class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.N = len(nums)
        if self.N > 0:
            self.T = list(nums) + list(nums)
            self.T[0] = 0
            for i in range(self.N-1, 0, -1):
                self.T[i] = self.merge(self.T[2*i], self.T[2*i+1])

    def merge(self, x, y):
        return x + y
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.T[i+self.N] = val
        x = i + self.N 
        while x > 1:
            self.T[x//2] = self.merge(self.T[x], self.T[x^1])
            x = x//2

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        l = i+self.N 
        r = j+self.N+1
        res = 0
        while l < r:
            if l%2 == 1:
                res = self.merge(res, self.T[l])
                l += 1
            if r%2 == 1:
                r -= 1
                res =  self.merge(res, self.T[r])
            l = l//2
            r = r//2
        return res
                

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)