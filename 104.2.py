def maxDepth(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if root is None:
        return 0
    
    ans = 0
    cur = [root]
    next = []

    while cur:
        next = []

        for node in cur:
            if node.left: next.append(node.left)
            if node.right: next.append(node.right)

        ans += 1
        cur = next

    return ans
