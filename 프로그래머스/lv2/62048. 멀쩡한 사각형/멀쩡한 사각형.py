from sys import stdin, stdout
import math


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))


if __name__ == "__main__":
    w = 8
    h = 12
    print(solution(w, h))