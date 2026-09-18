from typing import Final

PIN: Final[str] = "1234"
ATTEMPTS: Final[int] = 3

def input_pin(prompt: str = "Zadej pin: ", error_prompt: str = "Spatny format pinu.") -> str:
    while True:
        pin = input(prompt)
        if len(pin) == 4 and pin.isdigit():
            return pin

        print(error_prompt)


def check_pin(pin: str, correct_pin: str = PIN, attempts_left: int = ATTEMPTS) -> bool:
    return attempts_left > 0 and pin == correct_pin


attempts_left = ATTEMPTS
for i in range(1, attempts_left + 1):
    pin = input_pin()
    valid = check_pin(pin, attempts_left=attempts_left)
    attempts_left -= 1

    if valid:
        print("PIN zadany spravne.")
        break

    print(f"Spatne zadany pin. Zbyva {attempts_left} pokusu.")
