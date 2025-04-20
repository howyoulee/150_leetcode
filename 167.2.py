def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    i, j = 0, len(numbers)-1
    sum = []
    
    while i < j:
        sum = numbers[i] + numbers[j]
        
        if sum < target:
            i += 1
        if sum > target:
            j -= 1
        elif sum == target:
            return [i+1,j+1]
        
