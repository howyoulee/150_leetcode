def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
        
    # 初始化 9 个集合，用于存储每一行、每一列和每个 3x3 子盒子中出现的数字
    rows = [set() for _ in range(9)]  # 每一行的数字集合
    cols = [set() for _ in range(9)]  # 每一列的数字集合
    boxes = [set() for _ in range(9)]  # 每个 3x3 子盒子的数字集合，索引通过公式计算

    # 遍历整个数独棋盘
    for i in range(9):  # 遍历每一行
        for j in range(9):  # 遍历每一列
            val = board[i][j]  # 获取当前单元格的值
            if val == '.':  # 如果是空格，跳过
                continue

            # 检查当前数字是否已经在对应的行、列或 3x3 子盒子中出现
            if val in rows[i]:  # 检查当前行是否有重复数字
                return False
            if val in cols[j]:  # 检查当前列是否有重复数字
                return False
            box_index = (i // 3) * 3 + (j // 3)  # 计算当前数字所属的 3x3 子盒子的索引
            if val in boxes[box_index]:  # 检查当前 3x3 子盒子是否有重复数字
                return False

            # 如果没有重复，将数字添加到对应的行、列和 3x3 子盒子的集合中
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_index].add(val)

    # 如果遍历完成后没有发现重复数字，返回 True
    return True