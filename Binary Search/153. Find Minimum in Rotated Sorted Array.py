class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        
        start, end = 0, len(nums) - 1
        if nums[end] > nums[start]:
            return nums[start]
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[start] > nums[mid]:
                end = mid
            else:
                start = mid
    
        if nums[end] < nums[start]:
            return nums[end]
        return nums[start]
