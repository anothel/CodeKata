from sys import stdin, stdout
import math


def solution():
    stdout.write("n e\n")
    stdout.write("- -----------\n")
    answer: float = 0
    for i in range(10):
        stdout.write("%d " % i)
        answer += (1 / math.factorial(i))
        if answer > 2.5:
            stdout.write("%.9f\n" % answer)
        elif answer == 1 or answer == 2:
            stdout.write("%d\n" % answer)
        elif answer == 2.5:
            stdout.write("%.1f\n" % answer)


if __name__ == "__main__":
    solution()