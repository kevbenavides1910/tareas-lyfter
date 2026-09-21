import functools
from datetime import date


class User:
    date_of_birth: date

    def __init__(self, name: str, date_of_birth: date):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def require_adult_user(func):
    @functools.wraps(func)
    def wrapper(user: User, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError(
                f"[{func.__name__}] First argument must be a User instance."
            )
        if user.age < 18:
            raise PermissionError(
                f"[{func.__name__}] User '{user.name}' is {user.age} years old. "
                f"Must be 18 or older."
            )
        return func(user, *args, **kwargs)
    return wrapper


@require_adult_user
def restricted_action(user: User):
    print(f"Access granted for {user.name} (age {user.age}).")


if __name__ == "__main__":
    adult = User("Sarah", date(1990, 6, 15))
    minor = User("Kevin Jr.", date(2012, 3, 1))

    restricted_action(adult)
    try:
        restricted_action(minor)
    except PermissionError as e:
        print(e)
