def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(nums)-1 #[0, len(nums)-2]  [0, len(nums)-1)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left
