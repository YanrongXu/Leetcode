class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
            
        if n < 0:
            x = 1.0 / x
            n = abs(n)
        
        res = 1
        while n != 0:
            if n & 1:
                res *= x
            x *= x
            n = n >> 1
        return res
