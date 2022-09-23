"""
Функционал игры "чётные и нечётные числа"
"""
from random import randint
from .cli import welcome_user


def is_even(num: int) -> bool:
    """
    Фунция для проверки является ли число чётное или нет
    """
    if num % 2 == 0:  # Если число делится на 2 без остатка, то чётное
        return True
    return False


def even_number(name: str) -> None:
    """
    Функция для вычиления чётности значения
    """
    print("Answer 'yes' if the number is even otherwise answer 'no'!")
    player_result: int = 0  # Счётчик для ослеживания результата игрока (необ.)
    tries_count: int = 0  # Счётчик для отслеживания количества попыток
    while tries_count != 3:
        number: int = randint(1, 100)
        tries_count += 1  # Прибавляем количество ходов
        print(f"Question: {number}")
        player_answer: str = str(input("Your answer is: "))
        if (player_answer == 'yes' and is_even(number)) or \
           (player_answer == 'no' and not is_even(number)):
            player_result += 1
            print("Correct!")
        else:
            if is_even(number):
                print(f"{player_answer} is wrong answer ;(. "
                      f"Correct answer was 'no'")
            else:
                print(f"{player_answer} is wrong answer ;(. "
                      f"Correct answer was 'yes'")
            print(f"Let's try again, {name}!")
            break

    if player_result == 3:
        print(f"Congratulations, {name}!")


def main() -> None:
    """
    Функция для запуска игры
    """
    player_name: str = welcome_user()
    even_number(player_name)


if __name__ == '__main__':
    main()
