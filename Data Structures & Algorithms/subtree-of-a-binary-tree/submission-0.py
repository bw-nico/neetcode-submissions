# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        
        # 2. Check if they are the same starting here
        if self.isSame(root, subRoot):
            return True
        
        # 3. If not the same, search the left and right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSame(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        elif not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        return (self.isSame(tree1.left,tree2.left) and self.isSame(tree1.right,tree2.right))
        