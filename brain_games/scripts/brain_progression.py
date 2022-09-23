"""
Функционал игры "математическая последовательность"
"""
from random import randint
from .cli import welcome_user


def make_progression() -> tuple:
    """
    Фукнция помогает нам генерировать последовательность и получить
    результат игры
    """
    # Сколько итерации будет в последовательности
    number_of_iterations: int = 10
    # С какого значения начинается последовательност
    starting_number: int = randint(1, 100)
    # Параметр икрементирование
    increment_number: int = randint(1, 5)
    # Какой индекс значение, которое будет скрыто от участника
    random_index_of_hidden_number: int = randint(0, 10)
    # Параметр, где будет храниться последовательность
    progress: str = f'{starting_number} '
    # Скрытое значение
    hidden_number: int = 0
    for i in range(number_of_iterations):
        if random_index_of_hidden_number == i:
            starting_number += increment_number
            hidden_number: int = starting_number
            progress += '.. '
        else:
            starting_number += increment_number
            progress += f'{starting_number} '
    return progress, hidden_number


def find_progression(name: str) -> None:
    """
    Функция для определения результата последовательнотси
    """
    print("What number is missing in this progression?")
    player_result: int = 0  # Счётчик для ослеживания результата игрока (необ.)
    tries_count: int = 0  # Счётчик для отслеживания количества попыток
    while tries_count != 3:
        new_progression = make_progression()  # Получаем последовательность
        tries_count += 1  # Прибавляем количество ходов
        print(f"Question: {new_progression[0]}")
        player_answer: int = int(input("Your answer: "))
        if player_answer == new_progression[1]:
            player_result += 1
            print("Correct!")
        else:
            print(f"{player_answer} is wrong answer ;(. Correct"
                  f" answer is {new_progression[1]}")
            print(f"Let's try again, {name}!")
            break
    if player_result == 3:
        print(f"Congratulations, {name}!")


def main() -> None:
    """
    Функция для запуска игры
    """
    player_name = welcome_user()
    find_progression(player_name)


if __name__ == '__main__':
    main()
