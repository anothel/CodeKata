from sys import stdin, stdout
import math


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        x, w = map(int, stdin.readline().rstrip().split())
        if x >= w:
            stdout.write("0\n")
            continue
        stdout.write("%d\n" % (math.ceil(math.log(w / x) / math.log(2))))


if __name__ == "__main__":
    solution()
