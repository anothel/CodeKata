from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    answer: int = 0

    while n != 1:
        answer += 1
        if n % 2 != 0:
            n += 1
            continue
        n //= 2

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
