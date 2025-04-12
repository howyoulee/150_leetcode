class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = 0
        result = []
        num_map = {}

        for index, num in enumerate(nums):
            num_map[num] = index
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map and num_map[complement] != i:
                result.append(i)
                result.append(num_map[complement])
                return result