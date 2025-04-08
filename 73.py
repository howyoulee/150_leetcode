def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    rows = len(matrix)
    cols = len(matrix[0])
    firstRowZero = False
    firstColZero = False

    for r in range(rows):
        for c in range(cols):
            