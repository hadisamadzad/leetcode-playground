#https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=featured-list&envId=top-interview-questions
s = "dvdf"
expected = 3

n = len(s)
maxlen = 0
word_map = {}
start = 0

for i in range(n):
    char = s[i]
    is_char_in_map = char in word_map
    char_in_map_index = word_map[char] if is_char_in_map else None

    if not is_char_in_map:
        word_map[char] = i
        maxlen = max(maxlen, i - start + 1)

    elif char_in_map_index >= start:
        maxlen = max(maxlen, i - start)
        start = word_map[char] + 1
        word_map[char] = i

    else:
        maxlen = max(maxlen, i - start + 1)
        word_map[char] = i

print(expected, maxlen)
