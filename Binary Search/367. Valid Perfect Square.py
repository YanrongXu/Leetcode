class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if not num or num <= 0:
            return False
        
        start, end = 0, num
        
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid
            else:
                start = mid
                
        if end * end == num:
            return True
        if start * start == num:
            return True
        return False
