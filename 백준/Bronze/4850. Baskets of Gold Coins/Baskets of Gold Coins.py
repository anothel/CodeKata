from sys import stdin, stdout


def solve():
    while True:
        try:
            n, w, d, weight = map(int, stdin.readline().rstrip().split())
            answer: int = ((n * (n - 1) / 2 * w) - weight) / d
            stdout.write("%d\n" % answer if answer != 0 else "%d\n" % n)
        except:
            break


if __name__ == "__main__":
    solve()
