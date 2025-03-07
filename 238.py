def productExceptSelf(nums):
    n = len(nums)
    
    # Step 1: 计算左侧乘积
    left = [1] * n  # 存储左侧乘积
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    
    # Step 2: 计算右侧乘积，同时计算结果
    right = 1  # 右侧乘积
    for i in range(n - 1, -1, -1):
        left[i] = left[i] * right  # 当前 left[i] 乘以右侧乘积
        right *= nums[i]  # 更新右侧乘积
    
    return left  # left 现在是最终结果