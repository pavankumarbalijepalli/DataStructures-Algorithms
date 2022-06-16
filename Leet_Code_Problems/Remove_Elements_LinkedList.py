# Question: https://leetcode.com/problems/remove-linked-list-elements/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        prev = ListNode(None)
        curr = head
        while curr:
            if curr.val == val:
                if curr == head:
                    head = head.next
                    curr = head
                    continue
                else:
                    prev.next = curr.next
                    curr = head
            prev = curr
            curr = curr.next
        return (head)