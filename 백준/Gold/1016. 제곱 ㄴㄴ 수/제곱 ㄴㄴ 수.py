from sys import stdin, stdout
import math


def getPrime(min: int, max: int, primes: list) -> int:
    answer: int = max - min + 1
    i: int = 2
    while i * i <= max:
        num: int = min // (i * i)
        if min % (i * i) != 0:
            num += 1
        while num * (i * i) <= max:
            if primes[num * (i * i) - min] == False:
                primes[num * (i * i) - min] = True
                answer -= 1
            num += 1
        i += 1
    return answer


def solution():
    min, max = map(int, stdin.readline().rstrip().split())
    primes: list = [False for _ in range((max - min + 1))]

    stdout.write("%d\n" % getPrime(min, max, primes))


if __name__ == "__main__":
    solution()
