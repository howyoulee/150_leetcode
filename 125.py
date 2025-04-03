def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """

    result = []
    for char in s:
        if char.isalnum():
            result.append(char.lower())

    length = len(result)
    for i in range(0, length/2):
        if result[i] != result[length-1-i]:
            return False
        
    return True
    