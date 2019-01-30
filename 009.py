class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        q = []
        while x > 0:
            b = x%10
            q.append(b)
            x = x//10
        while len(q) > 1:
            if q[0] != q[-1]:
                return False 
            q = q[1:-1]
        if len(q) < 2:
            return True
        return False
        
