from sys import stdin, stdout
import math


def solution():
    s: list = (stdin.readline().rstrip())

    stdout.write("%d\n" %
                 (math.floor(s.count('B') / 2) + math.floor(s.count('C') / 2)))


if __name__ == "__main__":
    solution()
