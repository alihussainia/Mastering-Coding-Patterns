# Symmetric Tree

Question Number: 101

Link: <a href="https://leetcode.com/problems/symmetric-tree/">Symmetric Tree</a>

Question: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

```
Example#1:
Input: root = [1,2,2,3,4,4,3]
Output: true
```

```
Example#2:
Input: root = [1,2,2,null,3,null,3]
Output: false
```
# Understanding the Concept

### By Graphic
<img src="https://github.com/alihussainia/LeetCode-Python/blob/master/Binary_Tree/101-symmetric-tree/img/symmetric-tree-graphic.png" width="1000"/>

### By Graph
<img src="https://github.com/alihussainia/LeetCode-Python/blob/master/Binary_Tree/101-symmetric-tree/img/symmetric-tree-graph.png" width="1000"/>

### By Code

``` Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # let's make two trees
        left_tree=root
        right_tree=root

        def isMirror(left_tree, right_tree):
            # Check whether both are None, is yes, return True
            if left_tree == None and right_tree == None: 
                return True

            # Check whether left_tree value is not None but right_tree value is None, is yes, return False
            elif left_tree != None and right_tree == None:
                return False

            # Check whether left_tree value is None but right_tree value is not None, is yes, return False
            elif left_tree == None and right_tree != None:
                return False
            
            # if both are not None but not equal as well, return False
            elif (left_tree!=None and right_tree!=None) and (left_tree.val!=right_tree.val):
                return False
            
            # first check whether both left and right tree values are not None 
            # and then check whether they are both equal, 
            # if yes move to next line i.e. return. 
            # Now follow the key rules that are mentioned in the image above

            elif (left_tree!=None and right_tree!=None) and (left_tree.val==right_tree.val):  
                return (isMirror(left_tree.left, right_tree.right) and isMirror(left_tree.right, right_tree.left))
        
        # returns the bool i.e. with either true or false 
        return isMirror(left_tree, right_tree)
```
