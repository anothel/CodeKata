from sys import stdin, stdout
import math


def solution():
    a, b = map(int, stdin.readline().rstrip().split())

    for _ in range(math.gcd(a, b)):
        stdout.write("1")


if __name__ == "__main__":
    solution()
