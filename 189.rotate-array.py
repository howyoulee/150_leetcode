class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        k = k % length  # 让k的大小不大于数组的长度

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, length-1)
        reverse(0, k-1)
        reverse(k, length-1)

        return nums
