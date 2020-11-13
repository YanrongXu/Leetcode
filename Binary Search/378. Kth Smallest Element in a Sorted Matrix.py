# sorting
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rec = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                rec.append(matrix[i][j])
        rec.sort()
        return rec[k - 1]

# using min heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix) #in this question matrix is n*n, so both row and col is n
        
        pq = [(matrix[i][0], i , 0) for i in range(n)] # take out the first row
        # matrix[i][0] 是具体的值，后面 (i, 0) 是记录候选人在matrix中的位置，方便每次右移添加下一位候选人
        """
        print(pq)
        [(1, 0, 0), (10, 1, 0), (12, 2, 0)]
        """
        heapq.heapify(pq) # change it to heap
        
        for i in range(k - 1): #一共弹k次，这里还是k-1次，return的时候第一次
            num, x, y = heapq.heappop(pq) # 弹出候选人里最小一个
            if y != n - 1: #如果这一行还没被弹完
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1)) #加入这一行的下一个候选人
                
        return heapq.heappop(pq)[0]
        
# binary search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = n = len(matrix) # since the martix is n*n
        
        lo, hi = matrix[0][0], matrix[m-1][n-1]
        
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            count = self.num_of_less_or_equal(matrix, mid)
            if count < k:
                lo = mid
            else:
                hi = mid
        if self.num_of_less_or_equal(matrix, lo) >= k:
            return lo
        
        return hi
    
    def num_of_less_or_equal(self, matrix, target):
        m = n = len(matrix)
        i, j = m - 1, 0
        count = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count
            
