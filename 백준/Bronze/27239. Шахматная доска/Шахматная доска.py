from sys import stdin, stdout

import math


def solution():
    n: int = int(stdin.readline().rstrip())

    a: int = n % 8 if n % 8 != 0 else 8

    stdout.write("%s%d\n" % (chr(96 + a), math.ceil(n / 8)))


if __name__ == "__main__":
    solution()
