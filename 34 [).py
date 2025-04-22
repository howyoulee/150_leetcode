def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def find_index(nums, target):
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

    
    left, right = find_index(nums, target), find_index(nums, target+1) - 1 

    return [left, right] if left < right else [-1, -1]

