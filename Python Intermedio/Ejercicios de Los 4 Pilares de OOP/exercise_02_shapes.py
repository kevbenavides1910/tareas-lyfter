from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def calculate_area(self) -> float:
        return self.side ** 2

    def calculate_perimeter(self) -> float:
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)


def prompt_float(message: str) -> float:
    """Ask the user for a float value, retrying on invalid input."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def build_circle() -> Circle:
    """Ask the user for circle dimensions and return a Circle instance."""
    radius = prompt_float("  Enter radius: ")
    return Circle(radius=radius)


def build_square() -> Square:
    """Ask the user for square dimensions and return a Square instance."""
    side = prompt_float("  Enter side length: ")
    return Square(side=side)


def build_rectangle() -> Rectangle:
    """Ask the user for rectangle dimensions and return a Rectangle instance."""
    width = prompt_float("  Enter width: ")
    height = prompt_float("  Enter height: ")
    return Rectangle(width=width, height=height)


def print_shape_info(shape: Shape) -> None:
    """Print area and perimeter for a given shape."""
    print(f"  Area:      {shape.calculate_area():.2f}")
    print(f"  Perimeter: {shape.calculate_perimeter():.2f}")


if __name__ == "__main__":
    builders = {
        "1": ("Circle", build_circle),
        "2": ("Square", build_square),
        "3": ("Rectangle", build_rectangle),
    }

    print("Select a shape:")
    for key, (name, _) in builders.items():
        print(f"  {key}. {name}")

    choice = input("Enter option (1/2/3): ").strip()

    if choice not in builders:
        print("Invalid option.")
    else:
        name, builder = builders[choice]
        print(f"\n--- {name} ---")
        shape = builder()
        print_shape_info(shape)
