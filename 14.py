def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs:
        return ""

    prefix = strs[0]

    for str in strs:
        if len(str) == 0:
            return ""
        
        for i in range(0, min(len(prefix), len(str))):
            if prefix[i] != str[i]:
                prefix = prefix[:i]
                break
            else:
                prefix = prefix[:len(str)]

    return prefix