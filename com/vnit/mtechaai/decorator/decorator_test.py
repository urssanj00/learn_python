from functools import wraps

# wrapper add logs over the already defined function. decorator function helps
# add extra feature to a function without changing its code
def log_function_call(func):
    @wraps(func)
    def wrapper_add(*args, **kwargs):
        # log before function call
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")

        result = func(*args, **kwargs)  # actual function call

        #log after function call
        print(f"Function {func.__name__} returned {result}")

        return result
    return wrapper_add

@log_function_call
def add(a, b):
    return a + b

result = add(3, 4)
