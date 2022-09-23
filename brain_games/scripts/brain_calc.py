"""
Функционал игры "Арифметические вычисления"
"""
from random import randint, choice
from .cli import welcome_user


SIMPLE_ARITHMETIC_SYMBOLS = ['+', '-', '*']


def brain_calc(name: str) -> None:
    """
    Функция для вычисления арифметических задач
    """
    print("What is the result of the expression?")
    player_result: int = 0  # Счётчик для ослеживания результата игрока (необ.)
    tries_count: int = 0  # Счётчик для отслеживания количества попыток
    while tries_count != 3:
        first_number: int = randint(1, 10)
        second_number: int = randint(1, 10)
        operator: str = choice(SIMPLE_ARITHMETIC_SYMBOLS)
        tries_count += 1  # Прибавляем количество ходов
        answer_evaluation: float = eval(f"{first_number} {operator}"
                                        f" {second_number}")
        print(f"Question: {first_number} {operator} {second_number}")
        player_answer: float = float(input("Your answer: "))
        # Иногда получаем дробные числа, поэтому округляем на 2 цифры
        if player_answer == round(answer_evaluation, 2):
            player_result += 1
            print("Correct!")
        else:
            print(f"{player_answer} is wrong answer ;(. Correct "
                  f"answer is {round(answer_evaluation,2)}")
            print(f"Let's try again, {name}!")
            break
    if player_result == 3:
        print(f"Congratulations, {name}!")


def main() -> None:
    """
    Функция для тестирование
    """
    player_name: str = welcome_user()
    brain_calc(player_name)


if __name__ == '__main__':
    main()
