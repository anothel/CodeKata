from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    for _ in range(n):
        a, b = map(float, stdin.readline().rstrip().split())
        stdout.write("%.1f\n" % (round(abs(a - b), 1)))


if __name__ == "__main__":
    solution()
