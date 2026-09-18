def input_int(prompt: str | None = None) -> int:
    """
    Tries to get an integer from input. If success returns it, else ValueException is thrown.
    :param prompt: optional prompt for input
    :return: the inputted integer
    :raises ValueException: if the input isn't an integer
    """
    if prompt is None:
        x = input()
    else:
        x = input(prompt)
    return int(x)


def input_float(prompt: str | None = None) -> float:
    """
    Tries to get a float from input. If success returns it, else ValueException is thrown.
    :param prompt: optional prompt for input
    :return: the inputted float
    :raises ValueException: if the input isn't a float
    """
    if prompt is None:
        x = input()
    else:
        x = input(prompt)
    return float(x)
