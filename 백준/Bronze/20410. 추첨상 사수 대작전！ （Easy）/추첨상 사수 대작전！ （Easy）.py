from sys import stdin, stdout


def solve():
    m, seed, x1, x2 = map(int, stdin.readline().rstrip().split())

    a: int = 0
    c: int = 0
    for i in range(m):
        a = i
        if (x1 == (a * seed + c) % m and x2 == (a * x1 + c) % m):
            break
        for j in range(m):
            c = j
            if (x1 == (a * seed + c) % m and x2 == (a * x1 + c) % m):
                stdout.write("%d %d\n" % (a, c))
                return

    stdout.write("%d %d\n" % (a, c))


if __name__ == "__main__":
    solve()
