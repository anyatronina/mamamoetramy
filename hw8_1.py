def decorator(f):
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as ex:
            return ex
    return wrapper


@decorator
def func(a, b):
    return a / b


print(func(1, 2))
print(func(1, 'a'))
print(func(1, 0))
print(func(1))
print(func())
