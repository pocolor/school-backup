from typing import Callable


def input_repeat_check(prompt: str, check: Callable[[str], bool], error_prompt: str | None = None) -> str:
    while True:
        user_input = input(prompt)
        if not check(user_input):
            if error_prompt:
                print(error_prompt)
            continue

        return user_input


def check_base(base: str) -> bool:
    try:
        x = int(base)
        return x > 0
    except ValueError:
        return False


def check_exponent(exponent: str) -> bool:
    try:
        x = int(exponent)
        return x != 0
    except ValueError:
        return False


def input_base() -> int:
    return int(input_repeat_check("Zadej zaklad: ", check_base))


def input_exponent() -> int:
    return int(input_repeat_check("Zadej exponent: ", check_exponent))


base = input_base()
exponent = input_exponent()

result = 1
if exponent > 0:
    for i in range(1, exponent + 1):
        result *= base

elif exponent < 0:
    for i in range(1, abs(exponent) + 1):
        result /= base

print(result)
