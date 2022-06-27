from sys import stdin, stdout
import math


def solve():
    j = int(stdin.readline().rstrip())
    if j < 4:
        stdout.write("0\n")
        return
    stdout.write("%d\n" % (math.factorial(j - 1) //
                           (math.factorial(j - 4) * math.factorial(3))))


if __name__ == "__main__":
    solve()
