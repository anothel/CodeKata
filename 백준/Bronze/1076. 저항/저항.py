from sys import stdin, stdout
import math


def solution():
    d: dict = {
        "black": [0, 1],
        'brown': [1, 10],
        'red': [2, 100],
        'orange': [3, 1000],
        'yellow': [4, 10000],
        'green': [5, 100000],
        'blue': [6, 1000000],
        'violet': [7, 10000000],
        'grey': [8, 100000000],
        'white': [9, 1000000000]
    }

    answer: str = ''
    nAnswer: int = 0
    for i in range(3):
        if i == 2:
            nAnswer = int(answer)
            nAnswer *= int(d[stdin.readline().rstrip()][1])
            break
        answer += str(d[stdin.readline().rstrip()][0])
    stdout.write("%s\n" % nAnswer)


if __name__ == "__main__":
    solution()
