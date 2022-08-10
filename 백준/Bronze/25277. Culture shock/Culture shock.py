from itertools import count
from sys import stdin, stdout


def solution():
    _ = range(int(stdin.readline().rstrip()))
    sen: list = list(map(str, stdin.readline().rstrip().split()))

    stdout.write("%d\n" % (sen.count("she") + sen.count("her") +
                           sen.count("he") + sen.count("him")))


if __name__ == "__main__":
    solution()
