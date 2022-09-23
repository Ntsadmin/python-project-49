#!/usr/bin/env python
"""
Greeting module
"""
from .cli import welcome_user


def main() -> None:
    """
    getting the greetings to start the game
    """
    welcome_user()


if __name__ == '__main__':
    main()
