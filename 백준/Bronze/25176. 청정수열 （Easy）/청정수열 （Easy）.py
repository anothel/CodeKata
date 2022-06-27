from sys import stdin, stdout


def main():
    answer: int = 1
    for i in range(1, int(stdin.readline().rstrip()) + 1):
        answer *= i
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    main()