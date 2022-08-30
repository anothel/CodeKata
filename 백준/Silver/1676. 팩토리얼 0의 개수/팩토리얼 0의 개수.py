from sys import stdin, stdout
import math


def getAnswer(n: int) -> int:
    answer: int = 0
    start: bool = False
    while n > 0:
        if n % 10 == 0:
            if start == False:
                start = True
            answer += 1
        elif start == True:
            break
        n //= 10
    return answer


def solution():
    stdout.write("%d\n" %
                 getAnswer(math.factorial(int(stdin.readline().rstrip()))))


if __name__ == "__main__":
    solution()
