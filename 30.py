from collections import Counter

def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or not words:
        return []
    
    word_len  = len(words[0])
    words_num = len(words)
    substr_len = word_len * words_num
    words_counter = Counter(words)
    result = []

    for i in range(len(s) - substr_len + 1):
        seen = {}
        j = 0
        left = i
        count = 0
        
        for j in range(i, len(s) - word_len + 1):
            word = s[j:j + word_len]

            if word in words_counter:
                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > words_counter[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1
                
                if count == words_num:
                    result.append(left)
            else:
                seen.clear
                count = 0
                left = j + word_len

        return result