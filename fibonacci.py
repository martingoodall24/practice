#!/usr/bin/env python3

"""
Create a generalized class to create a fibonnaci
sequence based on a given number of input variables
and return the last 8 digits of the result. Do this
in an efficient manner.

"""


def last_8(some_int):
    """Return the last 8 digits of an int

    Parameters:
    some_int (int): the number in the sequence

    Returns:
    int: the last 8 digits of the seq value
    """
    last_8_digits = some_int % 100000000
    return last_8_digits


def optimized_fibonacci(f):
    """
    Creates fibonacci sequence based on
    specific initializers

    Parameters:
    f (int): position in fibonacci sequence

    Returns:
    int: the value in the fibonacci sequence

    """
    out = []
    out.append(0)
    out.append(1)
    for i in range(2, f + 1):
        out.append(out[i - 1] + out[i - 2])
    return out[f]


class SummableSequence(object):
    """ Class to generically calculate fibonacci sequence """

    def __init__(self, *initial):
        """
        The constructor for SummableSequence class.

        Parameters:
           initial (list): The list of initializer values.
        """
        self.initial = initial
        self.n = len(initial)

    def __call__(self, i):
        """
        Creates the fibonacci list

        Parameters:
           i (int): The final position in list of interest
        """
        out = []  # list to store sequence
        n = self.n
        j = 0  # counter
        # set the initials
        for each in self.initial:
            out.append(each)
        # sum the previous n values
        for j in range(0, i - n):
            a = sum(out[j : n + j + 1])
            out.append(a)
        return out[i - 1]


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
