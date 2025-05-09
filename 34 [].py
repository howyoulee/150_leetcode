def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def find_left(nums, target):
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def find_right(nums, target):
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right
    
    left, right = find_left(nums, target), find_right(nums, target)

    return [left, right] if left <= right else [-1, -1]

