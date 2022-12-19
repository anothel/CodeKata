from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    table: list = list(map(int, stdin.readline().rstrip().split()))
    cur: float = 1.0
    for i in range(n):
        cur *= (1 - table[i] / 100)
        stdout.write("%f\n" % ((1 - cur) * 100))


if __name__ == "__main__":
    solution()
