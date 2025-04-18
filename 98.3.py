def isValidBST(self, root):
    def f(node):
        if node is None:
            return float('inf'), float('-inf') # 全集
        
        left_min, left_max = f(node.left)
        right_min, right_max = f(node.right)

        x = node.val
        if x <= left_max or x >= right_min:
            return float('-inf'), float('inf') # 空集
        
        return min(left_min, x), max(right_max, x)
    
    return f(root)[1] != float('inf')
