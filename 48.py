def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    # 1. 转置（对角线对称）
    for i in range(n):
        for j in range(i + 1, n):  # j 从 i+1 开始，避免重复
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. 水平翻转（反转每一行）
    for row in matrix:
        row.reverse()