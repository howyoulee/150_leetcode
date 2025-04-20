def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    
    left = 0
    substr = ""
    ans = 0

    for right, char in enumerate(s):

        while char in substr:
            substr = substr[1:]
            left += 1
        substr += char
        ans = max(ans, len(substr)) # len(substr) == right - left + 1
    
    return ans
