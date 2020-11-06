# binary Search Solution
# By turing 2d array into 1d array
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return False
        start, end = 0, row * col - 1
        print(end)
        
        while start + 1 < end:
            mid = (start + end) // 2
            value = matrix[mid // col][mid % col]
            if value == target:
                return True
            else:
                if target < value:
                    end = mid
                else:
                    start = mid
        if matrix[end // col][end % col] == target:
            return True
        if matrix[start // col][start % col] == target:
            return True
        
        return False
