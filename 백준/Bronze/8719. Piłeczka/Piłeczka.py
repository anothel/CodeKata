from sys import stdin, stdout
import math


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        x, w = map(int, stdin.readline().rstrip().split())
        if x >= w:
            stdout.write("0\n")
            continue
        answer: int = math.ceil(math.log(w / x) / math.log(2))
        stdout.write("%d\n" % answer if answer != 0 else "1\n")


if __name__ == "__main__":
    solution()
