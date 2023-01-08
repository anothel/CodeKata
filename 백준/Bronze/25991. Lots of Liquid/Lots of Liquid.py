from sys import stdin, stdout
import math


def solution():
    n: int = int(stdin.readline().rstrip())
    c: list = list(map(float, stdin.readline().rstrip().split()))

    sum: float = 0.0

    for i in c:
        sum += math.pow(i, 3)

    stdout.write("%f\n" % (sum**(1.0 / 3.0)))


if __name__ == "__main__":
    solution()
