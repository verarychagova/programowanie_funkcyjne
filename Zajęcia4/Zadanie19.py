def check_anagrams(str1, str2):
    import re
    normalize = lambda s: ''.join(sorted(re.sub(r'[\W_]+', '', s.lower())))
    return normalize(str1) == normalize(str2)


print(check_anagrams("listen", "silent")) 