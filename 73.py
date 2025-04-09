def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    firstRowZero = any(matrix[0][j] == 0 for j in range(cols))
    firstColZero = any(matrix[i][0] == 0 for i in range(rows))

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix [0][c] == 0:
                matrix[r][c] = 0

    if firstRowZero:
        for c in range(cols):
            matrix[0][c] = 0

    if firstColZero:
        for r in range(rows):
            matrix[r][0] = 0

    return matrix