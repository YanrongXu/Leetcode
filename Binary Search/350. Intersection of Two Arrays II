class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        parent_set = dict()
        res = []
        
        for num in nums1:
            if num not in parent_set:
                parent_set[num] = 1
            else:
                parent_set[num] += 1
            
        for num in nums2:
            if num in parent_set and parent_set[num] != 0:
                res.append(num)
                parent_set[num] -= 1
                
        return res
