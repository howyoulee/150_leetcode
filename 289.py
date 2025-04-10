def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    directions = [  # 8 个方向
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    for i in range(m):
        for j in range(n):
            live_neighbors = 0
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    if abs(board[ni][nj]) == 1:
                        live_neighbors += 1
            
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = -1
            elif board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2
    
    for i in range(m):
        for j in range(n):
            if board[i][j] > 0:
                board[i][j] = 1
            else:
                board[i][j] = 0

    return board