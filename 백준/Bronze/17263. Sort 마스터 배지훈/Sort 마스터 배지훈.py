from sys import stdin, stdout


def main():
    int(stdin.readline().rstrip())
    nums: list = sorted(map(int, stdin.readline().rstrip().split()))
    stdout.write("%d\n" % nums[-1])


if __name__ == "__main__":
    main()
