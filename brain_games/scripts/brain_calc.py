"""
Functionality for the game "Arithmetic calculations"
"""
from brain_games.game_starter import run_game
from brain_games.utils import calc_util


def main() -> None:
    """
    Function to start the game
    """
    run_game(calc_util)


if __name__ == '__main__':
    main()
