"""
Основное начало игры
"""
import prompt


def welcome_user() -> str:
    """
    Функция для приветствия
    """
    print("Welcome to the Brain Games!")
    name: str = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    return name
