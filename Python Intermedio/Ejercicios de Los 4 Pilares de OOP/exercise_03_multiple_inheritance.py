class LogMixin:
    """Adds logging capability to any class."""

    def log(self, message: str) -> None:
        print(f"[{self.__class__.__name__}] {message}")


class SerializableMixin:
    """Adds basic serialization capability to any class."""

    def to_dict(self) -> dict:
        return self.__dict__


class Vehicle:
    def __init__(self, brand: str, speed: float):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount: float) -> None:
        self.speed += amount


class Car(LogMixin, SerializableMixin, Vehicle):
    def __init__(self, brand: str, speed: float, doors: int):
        super().__init__(brand, speed)
        self.doors = doors

    def accelerate(self, amount: float) -> None:
        self.log(f"Accelerating by {amount} km/h.")
        super().accelerate(amount)
        self.log(f"New speed: {self.speed} km/h.")


def prompt_float(message: str) -> float:
    """Ask the user for a float value, retrying on invalid input."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def prompt_int(message: str) -> int:
    """Ask the user for an integer value, retrying on invalid input."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def build_car() -> Car:
    """Ask the user for car details and return a Car instance."""
    brand = input("Enter car brand: ").strip()
    speed = prompt_float("Enter current speed (km/h): ")
    doors = prompt_int("Enter number of doors: ")
    return Car(brand=brand, speed=speed, doors=doors)


def run_car_demo(car: Car) -> None:
    """Ask the user how much to accelerate and show the result."""
    amount = prompt_float("Enter acceleration amount (km/h): ")
    car.accelerate(amount)
    print("\nCar data:")
    for key, value in car.to_dict().items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    print("--- Car Demo (Multiple Inheritance) ---")
    car = build_car()
    run_car_demo(car)
