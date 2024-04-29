def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Wystąpił błąd {e}")
            return None
    return wrapper

@safe_function
def divide(x, y):
    return x/y

print(divide(10, 2))
print(divide(10, 0))