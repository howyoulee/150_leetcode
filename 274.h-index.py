def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)  # 按降序排序
        h = 0
        for i, cite in enumerate(citations):
            if cite >= i + 1:
                h = i + 1
            else:
                break
        return h