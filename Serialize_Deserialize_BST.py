"""
Serialize and Deserialize BST
Medium
Topics
Companies
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]


Example 2:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 10**4].
0 <= Node.val <= 10**4
The input tree is guaranteed to be a binary search tree.



Approach 1: Postorder traversal to optimize space for the tree structure.
Intuition

Let's use here the fact that BST could be constructed from preorder or postorder traversal only. Please check this article for a detailed discussion. In brief, it's a consequence of two facts:

Binary tree could be constructed from preorder/postorder and inorder traversal.

Inorder traversal of BST is an array sorted in the ascending order: inorder = sorted(preorder).

That means that the BST structure is already encoded in the preorder or postorder traversal and hence they are both suitable for compact serialization.

Serialization could be easily implemented with both strategies, but for optimal deserialization better to choose the postorder traversal because member/global/static variables are not allowed here.

"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        def helper(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
        
        data = [int(x) for x in data.split(' ') if x]
        return helper()
    
def printTree(node, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printTree(node.right, level + 1)
    
if __name__ == "__main__":
    root = TreeNode(2)  ## [2,1,3]
    root.left = TreeNode(1)
    root.right =  TreeNode(3)
    
    data = Codec().serialize(root)
    res = Codec().deserialize(data)
    
    print(data)
    printTree(res)       