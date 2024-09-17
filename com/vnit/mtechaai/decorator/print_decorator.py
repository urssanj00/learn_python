from functools import wraps

def print_decorator(func):
    @wraps(func)
    def wrapper_print(*args, **kwargs):
        print(f'args={args} | kwargs={kwargs}')
    return wrapper_print

@print_decorator
def p(p, q):
    res = str(p) +":"+ str(q)
    print(f'res={res}')
    return res

res = p(99, 100)
print(f'res:{res}')

res = p(9, 10)
print(f'res:{res}')