def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    
    for i in range(len(s) - 1):
        if roman_map[s[i]] < roman_map[s[i + 1]]:  # 处理特殊情况
            ans -= roman_map[s[i]]
        else:
            ans += roman_map[s[i]]
    
    # 最后一个字符一定是正数，直接加上
    ans += roman_map[s[-1]]
    
    return ans