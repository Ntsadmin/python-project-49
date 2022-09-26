"""
Functional for 'Odd-even' brain game
"""
from random import randint

GAME_MESSAGE = "Answer 'yes' if the number is even otherwise answer 'no'!"


def is_even(number: int) -> bool:
    """
    :return True if number is even else False
    """
    if number % 2 == 0:
        return True
    return False


def game_utils() -> tuple:
    """
    :return question and correct answer
    """
    random_number: int = randint(1, 100)
    question: str = f"Question: {random_number}"
    if is_even(random_number):
        correct_answer: str = 'yes'
    else:
        correct_answer: str = 'no'
    return question, correct_answer
