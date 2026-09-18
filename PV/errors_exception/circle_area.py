import math

from input_funcs import input_float


def calculate_circle_area(radius: float) -> float:
    if radius <= 0:
        raise ArithmeticError("Radius must be greater than zero.")
    return math.pi * radius ** 2


def main() -> None:
    x = input_float("Zadej polomer: ")
    y = calculate_circle_area(x)
    print(y)


if __name__ == "__main__":
    main()
