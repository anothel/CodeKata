from sys import stdin, stdout


def solution():
    a, b, n = map(int, stdin.readline().rstrip().split())

    answer: int = 0

    for _ in range(n):
        a = a % b * 10
        answer = a // b

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
