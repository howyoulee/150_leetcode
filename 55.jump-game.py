class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        
        max_reach = 0
        for i in range(0, len(nums)-1):
            if i > max_reach:
                return False

            if max_reach < i + nums[i]:
                max_reach = i + nums[i]
            
            if max_reach >= len(nums) - 1:
                return True
            
        return False
            