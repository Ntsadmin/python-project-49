"""
Функционал игры "самый большой общий делитель"
"""
from math import gcd  # Встроенная функция для нахождения общего делителя
from random import randint
from .cli import welcome_user


def common_divisor(name: str) -> None:
    """
    Функция для нахождения общего делителя
    """
    print("Find the greatest common divisor of given numbers.")
    player_result: int = 0  # Счётчик для ослеживания результата игрока (необ.)
    tries_count: int = 0  # Счётчик для отслеживания количества попыток
    while tries_count != 3:
        first_number: int = randint(1, 10)
        second_number: int = randint(1, 10)
        number_divisor: int = gcd(first_number, second_number)
        tries_count += 1
        print(f"Question: {first_number} {second_number}")
        player_answer: int = int(input("You answer: "))
        if player_answer == number_divisor:
            player_result += 1
            print("Correct!")
        else:
            print(f"{player_answer} is wrong answer ;(. Correct"
                  f" answer is {number_divisor}!")
            print(f"Let's try again, {name}!")
            break

    if player_result == 3:
        print(f"Congratulations, {name}!")


def main() -> None:
    """
    Функция для запуска игры
    """
    player_name: str = welcome_user()
    common_divisor(player_name)


if __name__ == '__main__':
    main()
