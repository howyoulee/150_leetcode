def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    index_map = {}

    for index, num in enumerate(nums):
        if num in index_map and abs(index - index_map[num]) <= k:
            return True
        index_map[num] = index

    return False