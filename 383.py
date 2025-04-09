def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    # use Hashmap to create dictionary: get the frequency of each char
    dictionary = {}

    for char in magazine:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    for char in ransomNote:
        if char in dictionary and dictionary[char] > 0:
            dictionary[char] -= 1
        else:
            return False
        
    return True