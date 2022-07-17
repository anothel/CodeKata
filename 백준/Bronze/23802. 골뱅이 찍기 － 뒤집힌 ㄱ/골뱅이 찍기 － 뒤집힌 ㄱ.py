from sys import stdin, stdout


def print1(n: int):
    for _ in range(n):
        for _ in range(5 * n):
            stdout.write("@")
        stdout.write("\n")


def print2(n: int):
    for _ in range(4 * n):
        for _ in range(n):
            stdout.write("@")
        stdout.write("\n")


def solve():
    n: int = int(stdin.readline().rstrip())
    print1(n)
    print2(n)


if __name__ == "__main__":
    solve()
