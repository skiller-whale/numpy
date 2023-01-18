import numpy as np

"""
EXERCISE 2: Part 1
------------------------

* Instantiate a random number generator using `np.random.default_rng`.

The function `Generator.integers` can be used to draw
    random integers in a range. 

    * Use python's help function to find out what
        arguments `integers` takes.
    * Use it to draw coin tosses (draw `N_TOSSES` tosses)
        * We will consider a `0` to be tails and `1` - heads

The variable `win` contains the amount you win when the
    result is heads and the variable `loss` contains the
    amount you lose when the result is tails.
        * Calculate your winnings.

"""

N_TOSSES = 10
WIN = 0.25
LOSS = -0.25

# YOUR CODE GOES HERE
rng = ...
tosses = ...
total_winnings = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print('=' * 50)
# print('Game 1: Constant Winnings')
# if total_winnings == 0.0:
#     print("You didn't lose or win anything!")
# elif total_winnings < 0:
#     print(f"Oh, no, you lost {total_winnings:.2f}")
# else:
#     print(f"Congratulations, you won {total_winnings:.2f}")

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

HINT: What is the maximum amount you can win or lose?
    This will be the end point of your np.arange call.
"""


# YOUR CODE GOES HERE
win_values_per_round = ...
loss_values_per_round = ...

total_winnings = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print('=' * 50)
# print('Game 2: Progressive Winnings')
# if total_winnings == 0.0:
#     print("You didn't lose or win anything!")
# elif total_winnings < 0:
#     print(f"Oh, no, you lost {total_winnings:.2f}")
# else:
#     print(f"Congratulations, you won {total_winnings:.2f}")
