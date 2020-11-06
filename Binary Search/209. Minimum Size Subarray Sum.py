class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        total_length = float("inf")
        n = len(nums)
        sum_total = 0
        left = 0
        for right in range(n):
            sum_total += nums[right]
            while sum_total >= s:
                total_length = min(total_length, right - left + 1)
                sum_total -= nums[left]
                left += 1
        return 0 if total_length == float('inf') else total_length
