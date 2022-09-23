"""
Utilities for odd-even number
"""
from random import randint


def is_even(num: int) -> bool:
    """
    Function to check if the given number is even
    """
    if num % 2 == 0:  # The number is divided by 2 with rest
        return True
    return False


def get_even_number(player_result: int, tries_count: int, name: str) -> None:
    """
    the 'odd-even' game function
    """
    while tries_count != 3:
        number: int = randint(1, 100)
        tries_count += 1  # Increment the counter of attempts
        print(f"Question: {number}")
        player_answer: str = str(input("Your answer is: "))
        if (player_answer == 'yes' and is_even(number)) or \
           (player_answer == 'no' and not is_even(number)):
            player_result += 1
            print("Correct!")
        else:
            if is_even(number):
                print(f"{player_answer} is wrong answer ;(. "
                      f"Correct answer was 'no'")
            else:
                print(f"{player_answer} is wrong answer ;(. "
                      f"Correct answer was 'yes'")
            print(f"Let's try again, {name}!")
            break

    if player_result == 3:
        print(f"Congratulations, {name}!")
