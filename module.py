from functools import wraps

def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("logger called")
        return function()

    return wrapper


@logger
def foo():
    print("foo called")

