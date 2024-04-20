#%%

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p.val != q.val:
            return False
        
        left_comparison = Solution().isSameTree(p.left, q.left)
        right_comparison = Solution().isSameTree(p.right, q.right)

        return left_comparison and right_comparison


#%%

p = TreeNode(1,2,3)
q = TreeNode(1,2,3)

p.left

#%%

Solution().isSameTree(p, q)


#%%




#%%




#%%