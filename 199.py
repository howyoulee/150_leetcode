def rightSideView(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    ans = []
    
    def f(node, depth):
        if node is None:
            return
        
        if depth == len(ans):
            ans.append(node.val)

        f(node.right, depth+1)
        f(node.left, depth+1)

    f(root, 0)
    return ans
