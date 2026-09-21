import functools


def require_numbers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        all_values = list(args) + list(kwargs.values())
        for value in all_values:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"[{func.__name__}] Expected a number, "
                    f"got {type(value).__name__}: {value!r}"
                )
        return func(*args, **kwargs)
    return wrapper


@require_numbers
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print(multiply(4, 3))
    try:
        multiply(4, "oops")
    except TypeError as e:
        print(e)
