from operator import itemgetter  # 确保导入 itemgetter

def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if not intervals:
        return []
    
    intervals.sort(key=itemgetter(0))
    result = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= cur_end:
            cur_end = max(end, cur_end)
        else:
            result.append([cur_start, cur_end])
            cur_start, cur_end = start, end
        
    result.append([cur_start, cur_end])