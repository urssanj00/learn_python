from functools import wraps


def caching_result(func):
    cache_dictionary = {}
# test

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Make arguments and keyword arguments their own keys.
        caching_key = (args, tuple(kwargs.items()))
        print(f'args={args} | kwargs={kwargs} | caching_key={caching_key}')
        if caching_key not in cache_dictionary:
            cache_dictionary[caching_key] = func(*args, **kwargs)
        return cache_dictionary[caching_key]
    return wrapper

    @wraps(func)
    def wrapper_print(*args, **kwargs):

        print(f'args={args} | kwargs={kwargs}')
    return wrapper_print


# usage
@caching_result
def add(p, q):
    return p + q


@caching_result
def p(p, q):
    return str(p) + ":" + str(q)


res = p(99, 100)
result1 = add(1, 2)
result2 = add(4, 3)  # Doing so ought to bring up the cached outcome.
result3 = add(1, 2)

print(f'result1: {result1}')
print(f'result2: {result2}')
print(f'result3: {result3}')
print(f'res:{res}')
