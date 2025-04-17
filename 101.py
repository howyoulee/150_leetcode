def isSameTree(self, p, q):
    if p is None or q is None:
        return p is q
    
    return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

def isSymmetric(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    if root is None:
        return True
    
    return self.isSameTree(root.left, root.right)