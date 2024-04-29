def make_multiplier(value):
    def multiply():
        return value * 2

    return multiply


res = make_multiplier(3)
print(res())
