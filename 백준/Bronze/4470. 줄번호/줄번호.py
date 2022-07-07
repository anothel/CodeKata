from sys import stdin, stdout


def solve():
    for i in range(int(stdin.readline().rstrip())):
        stdout.write("%d. %s\n" % (i + 1, stdin.readline().rstrip()))


if __name__ == "__main__":
    solve()
