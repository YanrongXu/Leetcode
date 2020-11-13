# solution 1
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [i * i for i in A]
        
        return sorted(res)

# two pointer
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return []
        
        start, end = 0, len(A) - 1
        pos = end
        ans = [0] * len(A)
        while start <= end:
            if A[start] * A[start] > A[end] * A[end]:
                ans[pos] = A[start] * A[start]
                start += 1
            else:
                ans[pos] = A[end] * A[end]
                end -= 1
            pos -= 1
        return ans
