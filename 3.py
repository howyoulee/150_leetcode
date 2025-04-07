def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 1:
        return 1
    
    l, r = 0, 0
    substr = set()
    max_len = 0

    for r in range(0, len(s)):
        
        if s[r] not in substr:
            substr.add(s[r])
            max_len = max(max_len, len(substr))
        else:
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            max_len = max(max_len, len(substr))

    return max_len