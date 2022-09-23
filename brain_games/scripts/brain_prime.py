"""
Функционал игры "вычиление простых чисел"
"""
from random import randint
from .cli import welcome_user


def is_prime(num: int) -> bool:
    """
    Доп функция для определения, является ли число простое или нет
    """
    if num <= 1:  # Отрицательные числа не могут быть простыми
        return False
    # Проверяем если число делится на число больше 1 и меньше само число
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_number(name: str) -> None:
    """
    Функция для игры вычисления простых чисел
    """
    print("Answer 'yes' if the number is prime otherwise answer 'no'!")
    player_result: int = 0  # Счётчик для ослеживания результата игрока (необ.)
    tries_count: int = 0  # Счётчик для отслеживания количества попыток
    while tries_count != 3:
        number: int = randint(1, 1000)
        tries_count += 1  # Прибавляем количество ходов
        print(f"Question: {number}")
        player_answer: str = str(input("Your answer: "))
        if (player_answer == 'yes' and is_prime(number)) or \
           (player_answer == 'no' and not is_prime(number)):
            player_result += 1
            print("Correct !")
        else:
            if is_prime(number):
                print(f"{player_answer} is wrong answer ;(. "
                      f"Correct answer was 'yes'")
            else:
                print(f"{player_answer} is wrong answer ;(. "
                      f"Correct answer was 'no'")
            print(f"Let's try again, {name}!")
            break
    if player_result == 3:
        print(f"Congratulations, {name}!")


def main() -> None:
    """
    Функция для запуска игры
    """
    player_name: str = welcome_user()
    prime_number(player_name)


if __name__ == '__main__':
    main()
