from sys import stdin, stdout
import sys


def solution():
    cur: int = sys.maxsize
    answer: str = ''

    for _ in range(int(stdin.readline().rstrip())):
        t, h = map(str, stdin.readline().rstrip().split())
        if int(h) < cur:
            cur = int(h)
            answer = t
    stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solution()
