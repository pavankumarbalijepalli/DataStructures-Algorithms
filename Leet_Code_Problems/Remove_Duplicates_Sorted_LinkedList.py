# Question: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        d = set()
        curr = head
        while curr:
            if curr.val in d:
                prev.next = curr.next
                curr = curr.next
                continue
            d.add(curr.val)
            prev = curr
            curr = curr.next
        return head