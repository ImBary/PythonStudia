def group_words_by_length(words: list[str]) -> dict[int, list[str]]:
    pogrupowane = {}
    for word in words:
        length = len(word)
        if length not in pogrupowane:
            pogrupowane[length] = []
        pogrupowane[length].append(word)
    return pogrupowane


lista = ["kot", "pies", "dom", "auto", "drzewo"]
print(group_words_by_length(lista))
