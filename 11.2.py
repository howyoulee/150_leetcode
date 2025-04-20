def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height)-1
    amount = []
    max_amount = 0

    while left < right:
        amount = (right - left) * min(height[left], height[right])
        max_amount = max(amount, max_amount)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_amount

