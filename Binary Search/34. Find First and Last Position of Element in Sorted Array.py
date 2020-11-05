class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = -1, -1
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                left = self.find_prev(mid - 1, nums, target)
                right = self.find_next(mid + 1, nums, target)
                print(right)
                return [left, right]
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target and nums[end] == target:
            return [start, end]
        if nums[end] == target:
            return [end, end]
        if nums[start] == target:
            return [start, start]
        return [-1, -1]
    
    def find_prev(self, mid, nums, target):
        while mid >= 0 and nums[mid] == target:
            mid -= 1
        return mid + 1
    def find_next(self, mid, nums, target):
        while mid < len(nums) and nums[mid] == target:
            mid += 1
        return mid - 1
