import numpy as np
from utils import load_temperature_dataset


# pylint: disable=pointless-string-statement
"""
EXERCISE 3
------------------------

The function `load_temperature_dataset` loads a dataset of temperatures
    over 20 stations (and 12 months) for a town. It returns a list
    of 20 numpy arrays (each of size 12).

    * Calculate the average temperature for each month for the town.

    * Uncomment the tests below to test your results.

    * What's the average temperature in July?

"""

station_temps = load_temperature_dataset()

# YOUR CODE GOES HERE
average_temps = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert isinstance(average_temps, np.ndarray), "average_temps is not a numpy array!"
# assert average_temps.shape == (12, ), f"Shape of average temps ({average_temps.shape}) is wrong (should be {(12,)}!"
# assert np.isclose(average_temps[0], 5.26052991, rtol=1e-5), "January temperature is wrong!"
# assert np.isclose(average_temps[-1], 6.46125067, rtol=1e-5), "December temperature is wrong!"
