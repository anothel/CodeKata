from sys import stdin, stdout


def solve():
    b, w = map(int, stdin.readline().rstrip().split())
    if b == 0 and w == 0:
        stdout.write("Impossible\n")
        return
    if b == w:
        stdout.write("%d\n" % ((2 * min(b, w))**0.5))
    else:
        stdout.write("%d\n" % ((2 * min(b, w) + 1)**0.5))


if __name__ == "__main__":
    solve()
