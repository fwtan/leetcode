import math

class segment_tree_recursion:
    def __init__(self, A):
        self.build_segment_tree(A)

    def _get_mid_ind(self, s, e):
        return int(s + (e-s)//2)
    
    def merge(self, x, y):
        return x + y
        # return min(x, y)

    def build_segment_tree(self, A):
        n = len(A)
        n = 2 ** math.ceil(math.log2(n))
        n = 2 * n - 1
        self.A = A
        self.T = n * [-1]
        self.N = len(A)
        self._build_segment_tree_util(0, 0, self.N-1)

    def _build_segment_tree_util(self, tid, asid, aeid):
        assert(asid <= aeid)
        if asid == aeid:
            self.T[tid] = self.A[asid]
            # print('direct, tid, asid, aeid, val:', tid, asid, aeid, self.T[tid])
        else:
            amid = self._get_mid_ind(asid, aeid)
            tlid = 2 * tid + 1
            trid = 2 * tid + 2
            lv = self._build_segment_tree_util(tlid, asid, amid)
            rv = self._build_segment_tree_util(trid, amid+1, aeid)
            self.T[tid] = self.merge(lv, rv)
            # print('merged, tid, asid, aeid, val:', tid, asid, aeid, self.T[tid])
        return self.T[tid]

    def update_node(self, ind, val):
        diff = val - self.A[ind]
        self.A[ind] = val
        self._update_node_util(0, 0, self.N-1, ind, diff)

    def _update_node_util(self, tid, asid, aeid, auid, diff):
        if auid < asid or auid > aeid:
            return 
        self.T[tid] = self.T[tid] + diff 
        if asid < aeid:
            amid = self._get_mid_ind(asid, aeid)
            tlid = 2 * tid + 1
            trid = 2 * tid + 2
            self._update_node_util(tlid, asid, amid, auid, diff)
            self._update_node_util(trid, amid+1, aeid, auid, diff)
        
    def query(self, l, r):
        return self._query_util(0, 0, self.N-1, l, r-1)

    def _query_util(self, tid, asid, aeid, l, r):
        # [asid, aeid] in [l, r]
        if l <= asid and aeid <= r:
            # print('[tid, asid, aeid], ', tid, asid, aeid, self.T[tid])
            return self.T[tid]
        # [asid, aeid] and [l, r] have no intersection
        if r < asid or aeid < l:
            return 0
        amid = self._get_mid_ind(asid, aeid)
        tlid = 2 * tid + 1
        trid = 2 * tid + 2
        lv = self._query_util(tlid, asid, amid, l, r)
        rv = self._query_util(trid, amid+1, aeid, l, r)
        return self.merge(lv, rv)
        

class segment_tree_no_recursion:
    def __init__(self, A):
        self.build_segment_tree(A)
    
    def merge(self, x, y):
        return x + y
        # return min(x, y)

    def build_segment_tree(self, A):
        n = len(A)
        self.T = list(A) + list(A)
        for i in range(n-1, 0, -1):
            self.T[i] = self.merge(self.T[2*i], self.T[2*i+1])
        self.T[0] = 0
        self.N = n

    def update_node(self, ind, val):
        self.T[self.N+ind] = val
        i = self.N+ind 
        while i > 1:
            self.T[i//2] = self.merge(self.T[i], self.T[i^1])
            i = i//2
    
    def query(self, l, r):
        res = 0
        l += self.N; r += self.N 
        while l < r:
            if l%2 == 1:
                res = self.merge(res, self.T[l])
                l += 1
            if r%2 == 1:
                r -= 1
                res = self.merge(res, self.T[r])
            l = l//2
            r = r//2
        return res


if __name__ == '__main__':
    A = [19, 9, 8, 13, 1, 7, 18, 0, 19, 19, 10, 5, 15, 19, 0, 0, 16]
    # print(len(A))
    st1 = segment_tree_recursion(A)
    # print(st1.N)
    st2 = segment_tree_no_recursion(A)
    # print('st1: ', st1.T)
    # print('-------------')
    # print('st2: ', st2.T)
    st1.update_node(4, 5)
    st2.update_node(4, 5)
    print(st1.query(1, 6))
    print(st2.query(1, 6))

    
    