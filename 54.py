def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    if not matrix or not matrix[0]:
        return []

    result = []
    top, buttom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while left <= right and top <= buttom:
        for col in range(left, right+1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, buttom+1):
            result.append(matrix[row][right])
        right -= 1

        if top <= buttom:
            for col in range(right, left-1, -1):
                result.append(matrix[buttom][col])
            buttom -= 1

        if left <= right:
            for row in range(buttom, top-1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result