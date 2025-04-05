def minSubArrayLen(self, target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    window_sum = 0
    min_len = float('inf')

    for r in range(0, len(nums)):
        window_sum += nums[r]

        while window_sum >= target:
            min_len = min(min_len, r - l + 1)
            window_sum -= nums[l]
            l += 1

    return 0 if min_len == float('inf') else min_len

