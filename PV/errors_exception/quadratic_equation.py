from input_funcs import input_float
from math import sqrt


def print_quadratic_equation_roots(a: float, b: float, c: float):
    d = b ** 2 - 4 * a * c
    x1 = None
    x2 = None
    inverted_2a = None
    sqrt_d = None

    try:
        inverted_2a = 1 / (2 * a)
        sqrt_d = sqrt(d)

    except ZeroDivisionError:
        try:
            1 / b
        except ZeroDivisionError:
            x1 = x2 = c
        else:
            x1 = x2 = -c / b

    except ValueError:
        sqrt_d = d ** 0.5
        x1 = (-b + sqrt_d) * inverted_2a
        x2 = (-b - sqrt_d) * inverted_2a

    else:
        x1 = (-b + sqrt_d) * inverted_2a
        x2 = (-b - sqrt_d) * inverted_2a

    finally:
        print(f"x1 = {x1}, x2 = {x2}")


def main() -> None:
    print_quadratic_equation_roots(0, 0, 0)


if __name__ == "__main__":
    main()