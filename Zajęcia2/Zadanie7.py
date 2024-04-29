words = ["apple", "kiwi", "ananas"]
five_letter = filter(lambda word: len(word) > 5, words)

print(list(five_letter))
