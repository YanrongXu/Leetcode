class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        parent_set = set()
        child_set = set()
        res = []
        for num in nums1:
            parent_set.add(num)
            
        for num in nums2:
            if num in parent_set and num not in child_set:
                res.append(num)
                child_set.add(num)
        return res
