def levelOrder(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    
    ans = []
    cur = [root]

    while cur:
        next = []
        vals = []

        for node in cur:
            vals.append(node.val)
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
        cur = next
        ans.append(vals) 

    return ans
