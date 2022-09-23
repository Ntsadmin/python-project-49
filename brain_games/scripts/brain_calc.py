"""
Functionality for the game "Arithmetic calculations"
"""
from .cli import welcome_user
from .calc_utils import get_calc_result


SIMPLE_ARITHMETIC_SYMBOLS = ['+', '-', '*']


def brain_calc(name: str) -> None:
    """
    Function for arithmetic calculation problems
    """
    print("What is the result of the expression?")
    player_result: int = 0  # Counter for player's results
    tries_count: int = 0  # Counter for attempts
    get_calc_result(player_result, tries_count, name)


def main() -> None:
    """
    Testing function
    """
    player_name: str = welcome_user()
    brain_calc(player_name)


if __name__ == '__main__':
    main()
