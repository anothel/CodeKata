from sys import stdin, stdout
import math


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        a, b = map(int, stdin.readline().rstrip().split())
        stdout.write("%d %d\n" % (math.lcm(a, b), math.gcd(a, b)))


if __name__ == "__main__":
    solution()