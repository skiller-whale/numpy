import numpy as np

# pylint: disable=pointless-string-statement
"""
EXERCISE 2: Part 1
------------------------

* Instantiate the random number generator `rng` using `np.random.default_rng`.

The function `rng.integers` can be used to draw
    random integers in a range. 

    * Use python's help function to find out what
        arguments `integers` takes.

    * Use the function `rng.ingegers` to generate 10 random numbers
        that are either 0 or 1.
        * We will consider `0` to be tails and `1` to be heads

The variable `WIN` contains the amount you win when the
    result is heads and the variable `LOSS` contains the
    amount you lose when the result is tails.
        * Calculate your winnings.

HINT: You can loop over the array.
"""

N_TOSSES = 10
WIN = 0.25
LOSS = -0.25

# YOUR CODE GOES HERE
rng = ...
tosses = ...

# HINT: You might need to write a for loop
total_winnings = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print('=' * 50)
# print('Game 1: Constant Winnings')
# if total_winnings > 0:
#     print(f"Congratulations, you won {total_winnings:.2f}")
# elif total_winnings < 0:
#     print(f"Oh, no, you lost {total_winnings:.2f}")
# else:
#     print("You didn't lose or win anything!")

"""
EXERCISE 2: Part 2
------------------------

Instead of winning or losing a constant amount, in this
    version of the game, each toss progressively wins
    or loses more. The more you play, the more you can
    win (or lose, respectively).

The first coin toss wins and loses nothing (0.).

For each subsequent toss, the amount you win or lose goes up by 0.25.

So on toss 1 you would win 0.25 or lose 0.25.
    On toss 2 you would win 0.5 or lose 0.5, etc.

    * Use numpy's `arange` function to create two arrays
        that contain the winnings and losses for each round.

    * Calculate your winnings using those two arrays.

HINT: You can loop over the array.
HINT: What is the maximum amount you can win or lose?
    This will be the end point of your np.arange call.
"""


# YOUR CODE GOES HERE
win_values_per_round = ...
loss_values_per_round = ...

# HINT: You might need to write a for loop
total_winnings = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print('=' * 50)
# print('Game 2: Progressive Winnings')
# if total_winnings > 0:
#     print(f"Congratulations, you won {total_winnings:.2f}")
# elif total_winnings < 0:
#     print(f"Oh, no, you lost {total_winnings:.2f}")
# else:
#     print("You didn't lose or win anything!")