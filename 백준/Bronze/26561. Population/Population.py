from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        p, t = (map(float, stdin.readline().rstrip().split()))
        p += t // 4
        p -= t // 7
        stdout.write("%d\n" % (p))


if __name__ == "__main__":
    solution()
