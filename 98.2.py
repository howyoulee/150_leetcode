pre = float('-inf')

def isValidBST(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    if root is None:
        return True
    
    if not self.isValidBST(root.left):
        return False
    
    if root.val <= self.pre:
        return False
    self.pre = root.val
    return self.isValidBST(root.right)
