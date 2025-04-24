def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    def mid_Compare_end(mid):
        end = nums[-1]
        if nums[mid] > end:
            return target > end and nums[mid] >= target
        else:
            return target > end or nums[mid] >= target

    left, right = 0, len(nums) #[0, len(nums)-1] [0, len(nums))

    while left < right:
        mid = (left + right) // 2

        if mid_Compare_end(mid):
            right = mid
        else:
            left = mid + 1

    if nums[left] != target or left == len(nums):
        return -1

    return left
