# Question: https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        curr1 = list1
        curr2 = list2

        out = ListNode(None)
        temp = out
        
        while curr2 or curr1:
            if not curr1:
                out.next = curr2
                break
            
            if not curr2:
                out.next = curr1
                break

            if curr1.val <= curr2.val:
                node = ListNode(curr1.val)
                node.next = None
                out.next = node
                out = out.next
                curr1 = curr1.next

            elif curr2.val <= curr1.val:
                node = ListNode(curr2.val)
                node.next = None
                out.next = node
                out = out.next
                curr2 = curr2.next

        return temp.next