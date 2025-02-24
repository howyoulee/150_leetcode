class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        slow = 0
        fast = 1

        for fast in range(1, length):
            if nums[fast] != nums[slow]:
                nums[slow + 1] = nums[fast]
                slow += 1

        return slow + 1