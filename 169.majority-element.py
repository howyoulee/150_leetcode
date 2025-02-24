class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sorted()

        length = len(nums)

        return nums[length / 2]