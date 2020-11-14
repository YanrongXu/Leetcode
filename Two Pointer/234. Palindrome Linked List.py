# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# turn linked list into array then two pointer
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val = []
        while head is not None:
            val.append(head.val)
            head = head.next
        start, end = 0 , len(val) - 1
        while start <= end:
            if val[start] != val[end]:
                return False
            start += 1
            end -= 1
        return True

# 
