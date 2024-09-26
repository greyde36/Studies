def single_root_words(root_word, *other_words):
    same_word = []
    for i in range(len(other_words)):
        if other_words[i].lower().count(root_word.lower()) >= 1 or root_word.lower().count(other_words[i].lower()) >= 1:
            same_word.append(other_words[i])
    return same_word


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)