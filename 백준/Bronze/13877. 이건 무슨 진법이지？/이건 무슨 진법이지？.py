from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    for _ in range(n):
        a, b = map(int, stdin.readline().rstrip().split())
        stdout.write("%d %d %d %d\n" % (a, int(str(b), 8) if int(max(list(str(b)))) < 8 else 0, b, int(str(b), 16)))


if __name__ == "__main__":
    solution()
