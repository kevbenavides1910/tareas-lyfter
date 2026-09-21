import functools


def log_params_and_return(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{func.__name__}] params: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[{func.__name__}] return: {result}")
        return result
    return wrapper


@log_params_and_return
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(10, 5)
    add(a=3, b=7)
