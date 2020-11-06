# still use templete for binary search to solve this quesitn
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[start] == target:
                return True
            if nums[mid] > nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] == nums[start]:
                start += 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False
