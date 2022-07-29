from sys import stdin, stdout
import math


def getPrime(n: int, array: list):
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1


def solve():
    n = 1000
    array: list = [True for _ in range(n + 1)]
    getPrime(n, array)

    answer: list = [1, 2, 3, 4, 5]
    n = int(stdin.readline().rstrip())
    for i in range(n - 5):
        if i == n - 6:
            nNum: int = answer[-1]
            while True:
                nNum += 1
                if array[nNum] == True:
                    answer.append(nNum)
                    break

        else:
            answer.append(answer[-1] + 1)

    stdout.write("%d\n" % n)
    for i in answer:
        stdout.write("%d " % i)


if __name__ == "__main__":
    solve()
