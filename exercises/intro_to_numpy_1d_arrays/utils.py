"""
A utility module for the intro_to_numpy_1d_arrays session.

Contains profiling functions and data-loading functions.
"""

from pathlib import Path
import timeit
import numpy as np


DATA_PATH = Path(__file__).parent / 'data'
SECOND_TO_MS = 1_000


# This is a mathematical function, for which
#   uppercase N is well-defined.
# pylint: disable=invalid-name
def time_N_calls(func, N):
    """Times N calls of a function.

    Args:
        func (callable): The function to time.
        N (int): How many times to call func.

    Returns:
        np.array: An array of execution times.
    """
    times = []
    for _ in range(N):
        start = timeit.default_timer()
        func()
        end = timeit.default_timer()

        times.append(end - start)
    return np.array(times)

# N_calls is more appropriate than n_calls here (which is what snake_case would be).
# pylint: disable=invalid-name
def profile(func, start=1_000, stop=1_000_000, step=10, N_calls=25):
    """Profile a function over an interval.

    Args:
        func (callable): The function to profile.
        start (int, optional): Interval start.. Defaults to 1_000.
        stop (int, optional): Interval end.. Defaults to 1_000_000.
        step (int, optional): Interval multiplication step. Defaults to 25.

    Returns:
        np.array: An array of execution times (N_range x N_call).
    """
    curr = start
    print('=' * 50)
    print(f'Profiling function {func.__name__}(N).')
    print('N   \t Avg Time (ms.)\t +-  Std. (ms.)')
    all_call_times = []

    # loop through and print time information
    while curr <= stop:
        # convert time to milliseconds for readability
        times = time_N_calls(lambda: func(curr), N_calls) * SECOND_TO_MS

        print(f'{curr}\t {times.mean():.6f} \t {times.std():.6f}')

        curr *= step
        all_call_times.append(times)

    return np.array(all_call_times)
# pylint: enable=invalid-name


def load_temperature_dataset():
    """Loads a temperature dataset for 20 stations over 12 months.

    Returns:
        list: A list of np.array of size (12,) for each station,
    """
    return list(np.loadtxt(DATA_PATH / 'fake_station_temps.txt'))
