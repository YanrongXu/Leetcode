# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n == 0:
            return 0
        first_bad = 0
        start, end = 0, n
        if n == 1 and isBadVersion(n):
            return n
    
        while start + 1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            first_bad = start
        if isBadVersion(end):
            first_bad = end
        return first_bad
