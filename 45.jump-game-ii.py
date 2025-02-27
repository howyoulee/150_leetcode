class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        max_reach = 0
        min_move = 0
        cur_reach = 0
        for i in range(0, len(nums) - 1):

            if i + nums[i] > max_reach:
                max_reach = i + nums[i]

            if cur_reach == i:
                min_move += 1
                cur_reach = max_reach

                if cur_reach >= len(nums) - 1:
                    return min_move