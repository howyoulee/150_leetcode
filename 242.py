def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # use Hashmap to create dictionary: get the frequency of each char
    dict1 = {}
    dict2 = {}

    for char in s:
        dict1[char] = dict1.get(char, 0) + 1

    for char in t:
        dict2[char] = dict2.get(char, 0) + 1
    
    return dict1 == dict2