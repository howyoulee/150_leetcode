def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []
    nums.sort()
    # 0 <   i < j < k   < len(nums)-1
    for i in range(len(nums)-2):
        x = nums[i]
        j = i + 1
        k = len(nums)-1

        if i > 0 and x == nums[i-1]:
            continue
        
        while j < k:
            if nums[j] + nums[k] > -nums[i]:
                k -= 1
            elif nums[j] + nums[k] < -nums[i]:
                j += 1
            elif nums[i] + nums[j] + nums[k] == 0:
                ans.append([x, nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                
                k -= 1
                while k > j and nums[k] == nums[k+1]:
                    k -= 1
    
    return ans
