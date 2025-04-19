from collections import deque  # 导入 deque

def zigzagLevelOrder(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    
    ans = []
    q = deque([root])
    if_even = False

    while q:
        vals = []

        for _ in range(len(q)):
            node = q.popleft()
            vals.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(vals[::-1] if if_even else vals)

        if_even = not if_even

    return ans
