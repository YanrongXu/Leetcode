# 模板式做法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
    
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
                
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return end + 1
