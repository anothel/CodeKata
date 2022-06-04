from sys import stdin, stdout
import math


def solve():

  stdout.write("%d\n" % (math.factorial(int(stdin.readline().rstrip())) % 10))


if __name__ == "__main__":
    solve()
