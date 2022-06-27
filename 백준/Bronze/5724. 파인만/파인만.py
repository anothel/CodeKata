from sys import stdin, stdout


def main():
    while True:
        n: int = int(stdin.readline().rstrip())
        if n == 0:
            break
        answer: int = 0
        for i in range(1, n + 1):
            answer += (n - i + 1)**2
        stdout.write("%d\n" % answer)


if __name__ == "__main__":
    main()
