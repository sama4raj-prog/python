def match_words(words):

    count = 0
    list = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count =count + 1
            list.append(word)
    print(f"List of words with first and last letter same: {list}")
    return count
total_matching_words =  match_words(["aba","cfx", "cddddc", "xyz", "ab"])
print(total_matching_words)