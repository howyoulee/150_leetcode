def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()

        words = words[::-1]

        return ' '.join(words)