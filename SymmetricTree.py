#%%

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)


#%%





#%%






#%%