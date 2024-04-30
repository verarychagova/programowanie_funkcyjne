def capitalize_all_words(text):
    return ' '.join(word.capitalize() for word in text.split())

print(capitalize_all_words("hello world from python"))
