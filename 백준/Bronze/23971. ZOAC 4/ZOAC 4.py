from sys import stdin, stdout
import math


def solution():
    h, w, n, m = map(int, stdin.readline().rstrip().split())

    stdout.write("%d\n" % (math.ceil(h / (n + 1)) * math.ceil(w / (m + 1))))


if __name__ == "__main__":
    solution()
