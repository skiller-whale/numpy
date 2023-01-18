import numpy as np
from utils import profile

"""
EXERCISE 1
------------------------

Implement the two functions below to initialize a numpy array.

The `profile` function will profile the functions over different
values for `N` (different array sizes) and print out timing information.

    * `fill_with_zeros_from_list` should first create a python list
        of size N filled with zeros)and then convert it to a numpy array.
    * `fill_with_zeros_using_numpy` should use an appropriate
        call to a numpy function to create the array of zeros of size N.

"""


def fill_with_zeros_from_list(N):
    # YOUR CODE GOES HERE
    pass


def fill_with_zeros_using_numpy(N):
    # YOUR CODE GOES HERE
    pass

# <<< DO NOT CHANGE THE LINES BELOW HERE >>>
profile(fill_with_zeros_from_list)
profile(fill_with_zeros_using_numpy)
