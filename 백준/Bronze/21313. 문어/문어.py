from sys import stdin, stdout
import sys


def solution():
    n: int = int(stdin.readline().rstrip())

    for _ in range(n // 2):
        stdout.write("1 2 ")
    for _ in range(n % 2):
        stdout.write("3")


if __name__ == "__main__":
    solution()
