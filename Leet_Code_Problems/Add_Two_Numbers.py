# Question: https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a dummy node to store the output
        res = head = ListNode()

        # carry will hold the value 1 
        # if sum of two digits in greater than 9 else 0
        carry = 0
        
        # while there is something to add to solution
        while l1 or l2 or carry:
            # get values from lists that needs to be added,
            # if one list is None, it's respective value is 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # get total sum for that node
            _sum = val1 + val2 + carry
            
            # This will be remainder if sum>9
            val = _sum % 10

            # This will take the carry value if sum>9
            carry = _sum // 10

            # traverse to next node inside the list
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # this will add the sum to the linked list 
            # and move forward to read next values
            head.next = ListNode(val)
            head = head.next
        
        # since first value is null when we created it,
        # we will have our solution from the next part of the res node.
        return res.next