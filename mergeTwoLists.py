"""
Merge two sorted lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Approach 1: Recursion
Intuition

We can recursively define the result of a merge operation on two lists as
the following (avoiding the corner case logic surrounding empty lists):

list1[0]+merge(list1[1:],list2)  list1[0]<list2[0]
list2[0]+merge(list1,list2[1:])  otherwise
  
Namely, the smaller of the two lists' heads plus the result of a merge on
the rest of the elements.

Algorithm

We model the above recurrence directly, first accounting for edge cases.
Specifically, if either of l1 or l2 is initially null, there is no
merge to perform, so we simply return the non-null list. Otherwise, we
determine which of l1 and l2 has a smaller head, and recursively set the
next value for that head to the next merge result. Given that both lists
are null-terminated, the recursion will eventually terminate.


"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2