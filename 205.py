def isIsomorphic(self, s, t):
    d1, d2 = dict(), dict()
    for v, w in zip(s,t):
		    # 检查当前字符是否违反同构规则
        if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
                return False
        d1[v], d2[w] = w, v
    return True