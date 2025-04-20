from collections import Counter

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    
    left = 0
    conuter = Counter()
    ans = 0

    for right, char in enumerate(s):

        conuter[char] += 1
        while conuter[char] > 1:
            conuter[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)
    
    return ans
