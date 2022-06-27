from sys import stdin, stdout


def func(n: int) -> int:
    return n * (1 + n) // 2


def main():
    a, b = map(int, stdin.readline().rstrip().split())

    answer: int = 1
    for i in range(a, b + 1):
        answer *= func(i)

    stdout.write("%d\n" % (answer % 14579))


if __name__ == "__main__":
    main()