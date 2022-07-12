from sys import stdin, stdout


def solve():
    a, b, c = map(int, stdin.readline().rstrip().split())
    nCurrentCoin: int = 0
    nDay: int = 0
    while True:
        nDay += 1
        nCurrentCoin += a
        if nDay % 7 == 0:
            nCurrentCoin += b
        if nCurrentCoin >= c:
            break

    stdout.write("%d\n" % nDay)


if __name__ == "__main__":
    solve()
