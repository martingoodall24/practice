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
    signal.alarm

    def _timeout(signum, frame):
        raise TimeoutError()

    signal.signal(signal.SIGALRM, _timeout)

    @contextmanager
    def timeout(seconds=1, message="Timeout!"):
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
        t0 = time()
        yield
        if time() - t0 > seconds:
            raise TimeoutError(message)


@contextmanager
def capture_print():
    _stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = _stdout


class FibTests(TestCase):
    def test_fibonnacci(self):
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

    def test_summable(self):
       initializers = ([0,1], [5,7,11])])
       for each in initializers:
            ss = SummableSequence(each)
            for n in range(0, 50, 5):
                with timeout(message="Timeout running f({})".format(n)):
                        print(last_8(ss(n)))
                        with self.assertRaises(TimeoutError):
                            with timeout():
                                sleep(2)

    # def test_summable2(self):
    #     new_seq = SummableSequence(5, 7, 11)
    #     for n in range(0, 50, 5):
    #        with timeout(message="Timeout running f({})".format(n)):
    #             last_8(new_seq(n))
    #             with self.assertRaises(TimeoutError):
    #                 with timeout():
    #                     sleep(2)

class TestTimeout(TestCase):
    def test_timeout(self):
        with self.assertRaises(TimeoutError):
            with timeout():
                sleep(2)


class MiscTests(TestCase):
    def test_8(self):
        self.assertEqual(123, last_8(123))
        self.assertEqual(last_8(123456789), 23456789)


class PyramidTests(TestCase):
    def _assert_expected(self, rows, expected):
        with capture_print() as std:
            print_pyramid(rows)

        std.seek(0)
        captured = std.read()

        self.assertEqual(captured, expected)

    def test_pyramid_one(self):
        self._assert_expected(1, "=\n")

    def test_pyramid_two(self):
        self._assert_expected(2, "-=-\n" + "===\n")


if __name__ == "__main__":
    main()