class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 0, n
        
        while start <= end:
            mid = (start + end) // 2
            curr = mid * (mid + 1) // 2
            if curr == n:
                return mid
            if n < curr:
                end = mid - 1
            else:
                start = mid + 1
        return end
