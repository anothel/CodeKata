from sys import stdin, stdout


def solve():
    while True:
        num, diff, n = map(int, stdin.readline().rstrip().split())
        if num == 0 and diff == 0 and n == 0:
            break
        if (n - num) % diff == 0 and ((n - num) // diff + 1) > 0:
            stdout.write("%d\n" % ((n - num) // diff + 1))
        else:
            stdout.write("X\n")


if __name__ == "__main__":
    solve()
