def isSameTree(self, p, q):
    """
    :type p: Optional[TreeNode]
    :type q: Optional[TreeNode]
    :rtype: bool
    """
    if p is None or q is None:
        return p is q
    
    return p.val == q.val and self.isSameTree(self, p.left, q.left) and self.isSameTree(self, p.right, q.right)