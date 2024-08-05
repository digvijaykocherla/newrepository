def find_words_with_char(words, x):
    result = []
    for i, word in enumerate(words):
        if x in word:
            result.append(i)
    return result


words1 = ["abc", "bcd", "aaaa", "cbc"]
x1 = "a"
print(find_words_with_char(words1, x1))

words2 = ["abc", "bcd", "aaaa", "cbc"]
x2 = "z"
print(find_words_with_char(words2, x2))