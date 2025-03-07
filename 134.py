def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    n = len(gas)
    cur_gas = 0
    total_gas = 0
    balance = 0
    start = 1
    for i in range(0, n):
        balance = gas[i] - cost[i]
        cur_gas += balance
        total_gas += balance
        
        if cur_gas < 0:
            start = i + 1
            cur_gas = 0
        
    if total_gas < 0:
        return -1
    
    return start
