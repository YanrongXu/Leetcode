class Solution:
    def mySqrt(self, square: int) -> int:
        if not square or square == 0:
            return 0
        
        start, end = 0, square
        while start +1 < end:
            mid = (start + end) // 2
            if mid * mid == square:
                return mid
            elif mid * mid > square:
                end = mid
            else:
                start = mid
                
        if start * start == square:
            return start
        if end * end == square:
            return end
        return start
