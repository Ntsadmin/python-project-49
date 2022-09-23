"""
Utility module for game process
"""
from random import randint, choice


SIMPLE_ARITHMETIC_SYMBOLS = ['+', '-', '*']


def get_calc_result(player_result: int, tries_count: int, name: str) -> None:
    """
    The calc game function
    """
    while tries_count != 3:
        first_number: int = randint(1, 10)
        second_number: int = randint(1, 10)
        operator: str = choice(SIMPLE_ARITHMETIC_SYMBOLS)
        tries_count += 1  # Increment the counter of attempts
        if operator == '+':
            answer_evaluation = first_number + second_number
        elif operator == '-':
            answer_evaluation = first_number - second_number
        else:
            answer_evaluation = first_number * second_number
        print(f"Question: {first_number} {operator} {second_number}")
        player_answer: int = int(input("Your answer: "))
        if player_answer == answer_evaluation:
            player_result += 1
            print("Correct!")
        else:
            print(f"{player_answer} is wrong answer ;(. Correct "
                  f"answer is {answer_evaluation}")
            print(f"Let's try again, {name}!")
            break
    if player_result == 3:
        print(f"Congratulations, {name}!")
