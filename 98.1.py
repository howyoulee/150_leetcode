def isValidBST(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    if root is None:
        return True
    
    def check(node, left, right):
        if node is None:
            return True
        
        x= node.val

        return left < x < right and check(node.left, left, x) and check(node.right, x, right)

    check(root, float('-inf'), float('inf'))