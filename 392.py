def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) == 0:
        return True
    
    index = 0

    for char in t:
        if char == s[index] and index < len(s)-1:
            index += 1
    
    return index == len(s)
    