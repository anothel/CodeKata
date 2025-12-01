from sys import stdin


def solution(n):
    num = int(n)

    contains7 = '7' in n
    divisible7 = (num % 7 == 0)

    if not contains7 and not divisible7:
        print(0)
    elif not contains7 and divisible7:
        print(1)
    elif contains7 and not divisible7:
        print(2)
    else:
        print(3)


if __name__ == "__main__":
    n = (stdin.readline().strip())

    solution(n)
