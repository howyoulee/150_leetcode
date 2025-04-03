def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [""] * numRows
    index = 0
    down1_up0 = False #默认向上

    for letter in s:
        rows[index] += letter

        if index == 0 or index == numRows - 1:
            down1_up0 = not down1_up0
        
        if down1_up0:
            index += 1
        else:
            index -= 1

    return ''.join(rows)