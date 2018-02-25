"""
    File: craps.py
    This module studies and plays the game of craps.
"""

from die import Die


class Players(object):

    def __init__(self):
        """Has a pair of dice and a empty rolls list."""
        self._die1 = Die()
        self._die2 = Die()
        self._rolls = []

    def __str__(self):
        """Returns a string representation of the list of rolls"""
        result = ""
        for (v1, v2) in self._rolls:
            result = result + str((v1, v2)) + " " + str(v1 + v2) + "\n"
        return result

    def get_number_of_rolls(self):
        """Returns the number of the rolls."""
        return len(self._rolls)

    def play(self):
        """Plays a game, saves the rolls for that game, and resumes True for a win \
            and False for a loss."""
        self._rolls = []
        self._die1.roll()
        self._die2.roll()
        (v1, v2) = (self._die1.get_value(), self._die2.get_value())
        self._rolls.append((v1, v2))
        initial_sum = v1 + v2
        if initial_sum in (2, 3, 12):
            return False
        elif initial_sum in (7, 11):
            return True
        while True:
            self._die1.roll()
            self._die2.roll()
            (v1, v2) = (self._die1.get_value(), self._die2.get_value())
            self._rolls.append((v1, v2))
            sums = v1 + v2
            if sums == 7:
                return False
            elif sums == initial_sum:
                return True


def play_one_game():
    """Plays a single game and prints the results."""
    player = Players()
    you_win = player.play()
    print(player)
    if you_win:
        print("You win")
    else:
        print("You lose")


def play_many_game():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    wins = 0
    losses = 0
    win_rolls = 0
    loss_rolls = 0
    player = Players()

    for count in range(number):
        has_won = player.play()

        rolls = player.get_number_of_rolls()
        if has_won:
            wins += 1
            win_rolls += rolls
        else:
            losses += 1
            loss_rolls += rolls

    print("The total number of wins is ", wins)
    print("The total number of losses is ", losses)
    print("The average number of rolls per win %0.2f" % (win_rolls/wins))
    print("The average number of rolls per loss %0.2f" % (loss_rolls/losses))
    print("The winning percentage is %0.3f" % (wins / number))

if __name__ == "__main__":
    for i in range(3):
        play_one_game()