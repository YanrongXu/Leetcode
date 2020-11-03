# solution 1
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

# solution 2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        len1, len2 = len(nums1), len(nums2)
        res = []
        index1, index2 = 0, 0
        
        while index1 < len1 and index2 < len2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
                
        return res
