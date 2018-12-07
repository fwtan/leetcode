
class BITree:
    def __init__(self, A):
        self.build_binary_indexed_tree(A)

    def _last_set_bit(self, x):
        return x & (-x)

    def merge(self, x, y):
        return x + y

    def update_node(self, ind, val):
        x = ind + 1
        # print('-------------')
        # print(x)
        # print('/////')
        while x <= self.N:
            # print(x)
            self.T[x] = self.merge(self.T[x], val)
            x = x + self._last_set_bit(x)
               
    def build_binary_indexed_tree(self, A):
        n = len(A)
        self.N = n
        self.T = (n+1)*[0]
        for i in range(n):
            val = A[i]
            self.update_node(i, val)

    def query_node(self, ind):
        res = 0
        x = ind + 1
        while x > 0: 
            res = self.merge(res, self.T[x]) 
            x = x - self._last_set_bit(x)
        return res

    def query(self, l, r):
        return self.query_node(r-1) - self.query_node(l-1)


if __name__ == '__main__':
    A = [19, 9, 8, 13, 1, 7, 18, 0, 19, 19, 10, 5, 15, 19, 0, 0, 16]
    bit = BITree(A)
    # print(bit.T)
    print(bit.query(1, 6))
        



        