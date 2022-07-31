from sys import stdin, stdout


def solve():
    for _ in range(int(stdin.readline().rstrip())):
        a, b = map(int, stdin.readline().rstrip().split())
        stdout.write("%d\n" % ((a // b)**2))


if __name__ == "__main__":
    solve()
