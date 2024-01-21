from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# As LLs goes from LSB to MSB here, we don't need to reverse it
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        ln=node
        carry = 0

        while l1 or l2 or carry:    # Runs if either contains something to add

            # Assigning values to 2 numbers if they exist, else 0
            if l1:
                n1=l1.val
            else:
                n1=0
            
            if l2:
                n2=l2.val
            else:
                n2=0

            # Calculating the new digit
            _sum = n1+n2+carry
            carry=_sum//10
            _sum=_sum%10
            ln.next=ListNode(val=_sum)

            # Updating the values
            ln=ln.next
            if l1:
                l1=l1.next
            else:
                l1=None
            
            if l2:
                l2=l2.next
            else:
                l2=None
            
        return node.next
    
