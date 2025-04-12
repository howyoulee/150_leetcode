from collections import defaultdict

def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
    if not strs:
        return []
    
    anagrams = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())