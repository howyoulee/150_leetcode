def fullJustify(self, words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    result = []
    line_words = []
    line_len = 0

    for i in range(0, len(words)):
        if line_len + len(words[i]) > maxWidth:
            result.append(self.justify(line_words, maxWidth, is_last=False))
            line_words = []
            line_len = 0
        line_words.append(words[i])
        line_len = len(line_words)


    def justify(self, words, maxWidth, is_last):
        if is_last or len(words) == 1:
            return ' '.join(words).ljust(maxWidth)
        else:
            total_space = maxWidth - sum(len(w) for w in words)
            num_slots = len(words) - 1