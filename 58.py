def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    i = len(s) - 1
    strLen = 0

    while i >= 0 and s[i] == ' ':
        i -= 1
    
    while i >= 0 and s[i] != ' ':
        strLen += 1
        i -= 1
    
    return strLen