
is_palindrome = lambda s: (s := s.lower().replace(' ', '')) == s[::-1]

res = is_palindrome('tenet')
print(res)