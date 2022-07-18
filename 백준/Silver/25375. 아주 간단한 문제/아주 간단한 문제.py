from sys import stdin, stdout


def solve():
    for _ in range(int(stdin.readline().rstrip())):
        a, b = map(int, stdin.readline().rstrip().split())
        stdout.write("1\n" if (b % a == 0) and (b // a >= 2) else "0\n")


if __name__ == "__main__":
    solve()
