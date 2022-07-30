from sys import stdin, stdout


def solve():
    while True:
        m, a, b = map(int, stdin.readline().rstrip().split())
        if m == 0 and a == 0 and b == 0:
            break
        t: int = round(((m / a - m / b) * 3600))

        stdout.write("%d:%02d:%02d\n" % (t // 3600, (t % 3600) // 60, t % 60))


if __name__ == "__main__":
    solve()
