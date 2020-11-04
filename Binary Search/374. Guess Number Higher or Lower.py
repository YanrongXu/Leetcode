class Solution:
    def guessNumber(self, n: int) -> int:
        if not n or n < 1:
            return
        
        start, end = 0, n
        
        while start + 1 < end:
            mid = (start + end) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                end = mid
            else:
                start = mid
                
        if guess(end) == 0:
            return end
        if guess(start) == 0:
            return start
