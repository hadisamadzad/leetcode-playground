# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=featured-list&envId=top-interview-questions
def lengthOfLongestSubstring(s):
    n = len(s)

    maxlen = 0
    word_map = {}
    start = 0

    for i in range(n):
        char = s[i]

        if not char in word_map:
            word_map[char] = i
            maxlen = max(maxlen, i - start + 1)

        elif word_map[char] >= start:
            maxlen = max(maxlen, i - start)
            start = word_map[char] + 1
            word_map[char] = i

        else:
            maxlen = max(maxlen, i - start + 1)
            word_map[char] = i

    return maxlen


print(lengthOfLongestSubstring("pwwkew"))
