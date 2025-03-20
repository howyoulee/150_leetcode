def removeDuplicates(self, nums):    
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow