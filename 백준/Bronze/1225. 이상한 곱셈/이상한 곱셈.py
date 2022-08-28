from sys import stdin, stdout
import math


def solution():
    a, b = map(list, stdin.readline().rstrip().split())

    answer: int = 0

    for i in a:
        for j in b:
            answer += int(i) * int(j)

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
