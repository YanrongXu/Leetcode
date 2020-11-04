class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr or len(arr) < 3:
            return
        
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] > arr[mid - 1]:
                start = mid
            else:
                end = mid
        if arr[start] > arr[start + 1] and arr[start] > arr[start - 1]:
            return start
        else:
            return end
