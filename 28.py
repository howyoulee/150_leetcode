def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    if needle == '':
        return -1
    
    length = len(needle)
    str = ""
    def ifMatch(s, needle):
        return s == needle
    
    for i in range(0, len(haystack) - length + 1):
        if haystack[i] == needle[0]:
            str = haystack[i:i + length]
            if ifMatch(str, needle):
                return i
            else:
                continue

    return -1