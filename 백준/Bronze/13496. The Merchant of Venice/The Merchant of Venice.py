from sys import stdin, stdout


def solve():
    for i in range(int(stdin.readline().rstrip())):
        dookart: int = 0
        n, s, d = map(int, stdin.readline().rstrip().split())

        for j in range(n):
            di, vi = map(int, stdin.readline().rstrip().split())
            if di / s <= d:
                dookart += vi
        stdout.write("Data Set %d:\n" % (i + 1))
        stdout.write("%d\n\n" % dookart)


if __name__ == "__main__":
    solve()
