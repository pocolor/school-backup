from input_funcs import input_int


def input_int_loop(prompt: str | None = None, error_prompt: str | None = None) -> int:
    """
    Tries to get an integer from input. Loops until success.
    :param prompt: optional prompt for input
    :param error_prompt: optional prompt for error message
    :return: the inputted integer
    """
    while True:
        try:
            return input_int(prompt)
        except ValueError:
            if error_prompt is not None:
                print(error_prompt)


def main() -> None:
    x = input_int_loop("Zadej cislo: ")
    y = x + 1
    print(y)


if __name__ == "__main__":
    main()