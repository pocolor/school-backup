from math import sqrt, pi

from input_funcs import input_float


def signum(f: float) -> int:
    if f > 0:    return 1
    elif f < 0:  return -1
    else:        return 0


def thomson_algorithm(l: float, c: float) -> float:
    l_sign = signum(l)
    c_sign = signum(c)
    if l_sign * c_sign <= 0:
        raise ArithmeticError("negative number under square root")

    return 1 / (2 * pi * sqrt(l * c))


def main() -> None:
    L = input_float("Zadej indukcnost [H]:")
    C = input_float("Zadej kapacitu [F]:")
    F = thomson_algorithm(L, C)

    print("Frekvence je: " + str(F) + "Hz")


if __name__ == "__main__":
    main()