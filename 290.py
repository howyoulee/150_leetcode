def wordPattern(self, pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    words = s.split()

    if len(pattern) != len(words):
        return False
    
    char2word = {}
    word2char = {}

    for char, word in zip(pattern, words):
        if (char in char2word and char2word[char] != word) or (word in word2char and word2char[word] != char):
            return False

        char2word[char], word2char[word] = word, char

    return True