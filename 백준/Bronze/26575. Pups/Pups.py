from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    for _ in range(n):
        d, f, p = map(float, stdin.readline().rstrip().split())
        stdout.write("$%.2f\n" % (round(d * f * p, 2)))


if __name__ == "__main__":
    solution()
