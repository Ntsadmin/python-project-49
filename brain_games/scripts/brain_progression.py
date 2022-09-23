"""
Functional for mathematical progressions
"""
from random import randint, randrange
from .cli import welcome_user


def make_progression() -> tuple:
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
    return progress, hidden_number


def find_progression(name: str) -> None:
    """
    Function to determine the result of the game
    """
    print("What number is missing in this progression?")
    player_result: int = 0  # Counter for player's results
    tries_count: int = 0  # Counter for attempts
    while tries_count != 3:
        new_progression = make_progression()  # Get the progression
        tries_count += 1  # Increment the counter of attempts
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
    Function to start the game
    """
    player_name = welcome_user()
    find_progression(player_name)


if __name__ == '__main__':
    main()
