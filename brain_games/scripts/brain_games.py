#!/usr/bin/env python
"""
Скрипт приветствие игрока
"""
from .cli import welcome_user


def main() -> None:
    """
    Вызов приветствия
    """
    welcome_user()


if __name__ == '__main__':
    main()
