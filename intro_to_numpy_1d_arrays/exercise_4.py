import numpy as np

"""
EXERCISE 4
------------------------

In this exercise, you will use numpy's `Generator.integers` function again,
    this time to simulate dice rolls.

You can use python's help function to remind yourself of the
    arguments that `rng.integers` takes.

    * Instantiate the random number generator `rng`.
    * Draw `N_ROLLS` dice rolls (from 1, 6)
    * The variable `WIN` contains how much you win if you draw `6`
        * Calculate your winnings
    * Now set the random seed to `42`
        * Will you get the same result as other people in the session?
        * Why or why not?

"""

N_ROLLS = 100
WIN = 5.0

# YOUR CODE GOES HERE
rng = ...
dice_rolls = ...
total_winnings = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print('=' * 50)
# print('Game: Dice Rolls')
# if total_winnings == 0.0:
#     print("You didn't lose or win anything!")
# elif total_winnings < 0:
#     print(f"Oh, no, you lost {total_winnings:.2f}")
# else:
#     print(f"Congratulations, you won {total_winnings:.2f}")
