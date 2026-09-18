import re


def is_num_valid(number: str, minimum: int, maximum: int) -> bool:
    if not number.isdigit():
        return False

    return minimum <= int(number) <= maximum


def input_date_part(part: str, minimum: int, maximum: int) -> int:
    while True:
        input_part = input(f"Zadej {part.lower()}: ")
        if not is_num_valid(input_part, minimum, maximum):
            print(f"Musi byt cislo od {minimum} do {maximum}.")
            continue

        return int(input_part)

def input_day() -> int:
    return input_date_part("den", 1, 31)

def input_month() -> int:
    return input_date_part("mesic", 1, 12)

def input_year() -> int:
    return input_date_part("rok", 1000, 9999)

day = input_day()
month = input_month()
year = input_year()

print(f"{day}. {month}. {year}")