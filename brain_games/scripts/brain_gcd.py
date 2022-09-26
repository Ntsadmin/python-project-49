"""
'The largest common divider' game
"""
from brain_games.game_starter import run_game
from brain_games.utils import gcd_utils


def main() -> None:
    """
    Function to start the game
    """
    run_game(gcd_utils)


if __name__ == '__main__':
    main()
