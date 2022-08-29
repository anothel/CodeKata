from sys import stdin, stdout
import math


def isFalindrom(sen: str) -> int:
    left: int = 0
    right: int = len(sen) - 1

    while left < right:
        if sen[left] == sen[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1:
                tmp: str = sen[:right] + sen[right + 1:]
                if tmp == tmp[::-1]:
                    return 1
            if left + 1 < right:
                tmp: str = sen[:left] + sen[left + 1:]
                if tmp == tmp[::-1]:
                    return 1
            return 2
    return 0


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        stdout.write("%d\n" % isFalindrom(stdin.readline().rstrip()))


if __name__ == "__main__":
    solution()
