def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(nums)-1 #[0, len(nums)-2] [0, len(nums)-1)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[-1]:
            right = mid
        else:
            left = mid + 1
    
    return nums[left]

