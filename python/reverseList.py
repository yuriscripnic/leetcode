"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


current.next

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node  = None
        current_node = head
        while(current_node):
            next_node = current_node.next            
            current_node.next = previous_node            
            previous_node = current_node              
            current_node = next_node
        return previous_node    
    

def print_nodes(head: Optional[ListNode]):
    print("[",end=" ")
    while(head):
           print(head.val, end=" ")
           head = head.next
    print("]")

        
if __name__ == "__main__":    
    ex1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print_nodes(Solution().reverseList(ex1)) # [5,4,3,2,1]   
    
    ex2 = ListNode(1,ListNode(2))
    print_nodes(Solution().reverseList(ex2)) # [2,1]    
    print_nodes(Solution().reverseList(None)) # [] 