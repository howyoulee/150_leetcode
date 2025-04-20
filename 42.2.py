def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    ans = 0
    n = len(height)
    pre_max, suf_max = 0, 0
    left, right = 0, n-1
    
    while left < right:
        pre_max = max(pre_max, height[left])
        suf_max = max(suf_max, height[right])

        if pre_max < suf_max:
            ans += (pre_max - height[left]) * 1
            left += 1
        else:
            ans += (suf_max - height[right]) * 1
            right -= 1
    return ans

