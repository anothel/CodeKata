from sys import stdin, stdout
import sys


def solution():
    n, m, b = map(int, stdin.readline().rstrip().split())

    lvalue: list = list()

    answer: int = sys.maxsize
    height: int = 0
    for _ in range(n):
        lvalue.append(list(map(int, stdin.readline().rstrip().split())))

    for cur in range(257):
        maxH: int = 0
        minH: int = 0

        for i in range(n):
            for j in range(m):
                if lvalue[i][j] >= cur:
                    maxH += lvalue[i][j] - cur
                else:
                    minH += cur - lvalue[i][j]

        if maxH + b >= minH:
            if minH + (maxH * 2) <= answer:
                answer = minH + (maxH * 2)
                height = cur

    stdout.write("%d %d\n" % (answer, height))


if __name__ == "__main__":
    solution()
