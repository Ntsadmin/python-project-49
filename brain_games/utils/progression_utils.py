"""
Functional for "mathematical progression" brain game
"""
from random import randint, randrange

GAME_MESSAGE: str = "What number is missing in this progression?"


def game_utils() -> tuple:
    """
        Function that generates a progression with the hidden
        number to find by the player
        """
    # Iteration for the progression
    number_of_iterations: int = 10
    # Starting number of the progression
    starting_number: int = randint(1, 100)
    # Increments the starting number and etc...
    increment_number: int = randint(1, 5)
    # Which indexed number will be hidden
    random_index_of_hidden_number: int = randrange(number_of_iterations)
    # Parameter, that stores the progression
    progress: str = f'{starting_number} '
    # hidden number
    hidden_number: int = 0
    for i in range(number_of_iterations):
        if random_index_of_hidden_number == i:
            starting_number += increment_number
            hidden_number = starting_number
            progress += '.. '
        else:
            starting_number += increment_number
            progress += f'{starting_number} '
    return progress, str(hidden_number)
