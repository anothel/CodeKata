from sys import stdin, stdout
import math


def getPrime(n: int, array: list):
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1


def solution():
    n = 10**6
    primes: list = [True for _ in range(n + 1)]
    getPrime(n, primes)

    for _ in range(int(stdin.readline().rstrip())):
        s: int = int(stdin.readline().rstrip())
        appropriate: bool = True

        for i in range(2, len(primes)):
            if primes[i] == True and s % i == 0:
                stdout.write("NO\n")
                appropriate = False
                break
        if appropriate:
            stdout.write("YES\n")


if __name__ == "__main__":
    solution()
