#!/usr/bin/env python3

"""
Main test code for Problem Set 0 for CSCI-E-29

Test the fibonnaci and pyramid code

Classes:
    - Fibonnaci tests - FibTests
    - Pyramid tests - PyramidTests
    - Time out tests - TestTimeout
    - Miscellaneous tests - MiscTests

"""

import signal
import sys
from contextlib import contextmanager
from io import StringIO
from time import sleep, time
from unittest import TestCase, main

from fibonacci import SummableSequence
from fibonacci import last_8, optimized_fibonacci
from pyramid import print_pyramid

try:
    # Absent on Windows, trigger AttributeError

    def _timeout(signum, frame):
        raise TimeoutError()

    signal.signal(signal.SIGALRM, _timeout)
    signal.alarm

    @contextmanager
    def timeout(seconds=1, message="Timeout!"):
        """ Issue the actual timeout with message """
        # NB: doesn't work on windows
        signal.alarm(seconds)
        try:
            yield
        except TimeoutError:
            raise TimeoutError(message)
        finally:
            signal.alarm(0)


except AttributeError:

    @contextmanager
    def timeout(seconds=1, message="Timeout!"):
        """ Print timeout error message """
        t_0 = time()
        yield
        if time() - t_0 > seconds:
            raise TimeoutError(message)


@contextmanager
def capture_print():
    """ Get printout """
    _stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = _stdout


class FibTests(TestCase):
    """ Tests for fibonnacci use cases """

    def test_fibonnacci(self):
        """
        Compare the fibonacci results with expected
        """

        for n, expected in [
            # Check progressively more complex values, see if time out
            (0, 0),
            (1, 1),
            (6, 8),
            (10, 55),
            (15, 610),
            (20, 6765),
            (30, 832040),
            (40, 102334155),
            (100, 354224848179261915075),
        ]:
            with timeout(message="Timeout running f({})".format(n)):
                self.assertEqual(optimized_fibonacci(n), expected)

    def test_summable_2init(self):
        """ Tests for 2 initializers """
        ss = SummableSequence(0, 1)
        for n in range(0, 50, 5):
            with timeout(message="Timeout running f({})".format(n)):
                last_8(ss(n))
                with self.assertRaises(TimeoutError):
                    with timeout():
                        sleep(2)

    def test_summable_3inits(self):
        """ Tests for 3 initializers """
        new_seq = SummableSequence(5, 7, 11)
        for n in range(0, 100, 10):
            with timeout(message="Timeout running f({})".format(n)):
                last_8(new_seq(n))
                with self.assertRaises(TimeoutError):
                    with timeout():
                        sleep(2)


class TestTimeout(TestCase):
    """ Make sure it doesn't run too long """

    def test_timeout(self):
        """ raise error if it times out """
        with self.assertRaises(TimeoutError):
            with timeout():
                sleep(2)


class MiscTests(TestCase):
    """ Various tests that don't have their own category """

    def test_8(self):
        """ Make sure results of last_8() are as expected """

        self.assertEqual(123, last_8(123))
        self.assertEqual(last_8(123456789), 23456789)


class PyramidTests(TestCase):
    """ Test the pyramid code """

    def _assert_expected(self, rows, expected):
        """
        Confirm results are as expected for the pyramid code

        Parameters:
        rows (int): number of rows to generate in pyramid.
        expected: the results to compare to.
        """

        with capture_print() as std:
            print_pyramid(rows)

        std.seek(0)
        captured = std.read()

        self.assertEqual(captured, expected)

    def test_pyramid_one(self):
        """ test pyramid with 1 row """
        self._assert_expected(1, "=\n")

    def test_pyramid_two(self):
        """ test pyramid with 2 rows """
        self._assert_expected(2, "-=-\n" + "===\n")


if __name__ == "__main__":
    main()
