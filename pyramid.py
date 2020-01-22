#!/usr/bin/env python3
"""Print a pyramid to the terminal
A pyramid of height 3 would look like:
--=--
-===-
=====
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height
    :param int rows: total height
    """
    n = rows
    width = n + (n - 1)
    b = "-"
    z = ""
    seq = list(range(0, n * 2, 2))
    seq.sort(reverse=True)
    for i in seq:
        q = z.center(width - i, "=")
        q2 = "{s:{c}^{n}}".format(s=q, n=width, c=b)
        print(q2)


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
