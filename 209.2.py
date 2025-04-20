def minSubArrayLen(self, target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    ans = n+1
    sum = 0
    left = 0

    for right, val in enumerate(nums): # val: nums[right]
        sum += val
        
        while sum - nums[left] >= target:
            left += 1
            sum -= nums[left]

        if sum >= target:
            ans = min(ans, right - left + 1)
    
    return ans if ans <= n else 0