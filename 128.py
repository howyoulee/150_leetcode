def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    
    nums = sorted(nums)
    result = 1
    cur_count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            cur_count += 1
        elif nums[i] == nums[i-1]:
            continue
        else:
            result = max(cur_count, result)
            cur_count = 1

    return max(cur_count, result)