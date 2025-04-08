from collections import Counter

def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if not s or not t:
        return ""
    
    t_counter = Counter
    window = {}

    have, need = 0, len(t_counter)
    result = ""
    result_len = float("inf")
    left = 0

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1
        
        if c in t_counter and window[c] == t_counter[c]:
            have += 1

        while have == need:
            if (right - left + 1) < result_len:
                result = s[left:right+1]
                result_len = right - left + 1

            window[s[left]] -= 1
            if s[left] in t_counter and window[s[left]] < t_counter[s[left]]:
                have -= 1
            left += 1

    return result