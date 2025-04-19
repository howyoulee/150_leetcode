from collections import deque  # 导入 deque

def findBottomLeftValue(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if root is None:
        return []
    
    q = deque([root])

    while q:
        node = q.popleft()
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)

    return node.val
