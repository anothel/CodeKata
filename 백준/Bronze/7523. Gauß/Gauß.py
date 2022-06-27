from sys import stdin, stdout


def main():
    for p in range(int(stdin.readline().rstrip())):
        a, b = map(int, stdin.readline().rstrip().split())
        stdout.write("Scenario #%d:\n" % (p + 1))
        stdout.write("%d\n\n" % ((b - a + 1) * (a + b) // 2))


if __name__ == "__main__":
    main()