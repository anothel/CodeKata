from sys import stdin, stdout
import math


def solve():
    ht: float = int(stdin.readline().rstrip()) / 2
    stdout.write("%d\n" % int(ht * ht + 0.5))


if __name__ == "__main__":
    solve()
