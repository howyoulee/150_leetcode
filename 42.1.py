def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    pre_max = [0] * len(height)
    pre_max[0] = height[0]
    for i in range(1, len(height)):
        pre_max[i] = max(pre_max[i-1], height[i])
        
    suf_max = [0] * len(height)
    suf_max[len(height)-1] = height[len(height)-1]
    for i in range(len(height)-2, -1, -1):
        suf_max[i] = max(suf_max[i+1], height[i])

    ans = 0

    for cur_height, left_height, right_height in zip(height, pre_max, suf_max):
        ans += (min(left_height, right_height) - cur_height) * 1 # width 1 unit

    return ans

