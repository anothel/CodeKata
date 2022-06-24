from sys import stdin, stdout


def solution():
    answer: int = 0
    for i in range(1, int(stdin.readline().rstrip()) + 1):
        answer += i ** 3

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
