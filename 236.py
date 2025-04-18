def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root is None or root is p or root is q:
        return root # 如果此时底部node 他的左子右子都是空，则会直接放回root（None），所以这个node的放回到上一级node的值就是None

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    
    if left:
        return left
    
    return right 
