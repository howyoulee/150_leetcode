def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None
    
    x = root.val

    if p.val < x and q.val < x:
        return self.lowestCommonAncestor(root.left, p, q)
    
    if p.val > x and q.val > x:
        return self.lowestCommonAncestor(root.right, p, q)
    
    return root

