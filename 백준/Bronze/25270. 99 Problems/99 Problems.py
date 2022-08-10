from itertools import count
from sys import stdin, stdout


def getCount(n: int) -> int:
    answer: int = 0
    while n > 0:
        n //= 10
        answer += 1
    return answer


def solution():
    n = int(stdin.readline().rstrip())
    if n < 149:
        stdout.write("99\n")
        return

    next99: int = (n - n % 100) + 99
    befo99: int = next99 - 100
    stdout.write("%d\n" % befo99 if n - befo99 < next99 - n else "%d\n" %
                 next99)


if __name__ == "__main__":
    solution()
