class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        index_s, index_t = 0, 0
        
        while index_s < len_s and index_t < len_t:
            if s[index_s] == t[index_t]:
                index_s += 1
            index_t += 1
            
        return index_s == len_s
