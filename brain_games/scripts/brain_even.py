"""
'Even Odd' game
"""
from .cli import welcome_user
from .even_utils import get_even_number


def even_number(name: str) -> None:
    """
    Function to determine the result of the game
    """
    print("Answer 'yes' if the number is even otherwise answer 'no'!")
    player_result: int = 0  # Counter for player's results
    tries_count: int = 0  # Counter for attempts
    get_even_number(player_result, tries_count, name)


def main() -> None:
    """
    Function to start the game
    """
    player_name: str = welcome_user()
    even_number(player_name)


if __name__ == '__main__':
    main()
