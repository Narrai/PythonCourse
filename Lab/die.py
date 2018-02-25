"""File: die.py
   This module defines the Die class
"""

from random import randint


class Die(object):
    """This clas represents a six-sided die."""

    def __init__(self):
        """The initial face of the die."""
        self._value = 1

    def roll(self):
        """Reset the die's value to a random number"""
        self._value = randint(1, 6)

    def get_value(self):
        return self._value

    def __str__(self):
        return str(self._value)