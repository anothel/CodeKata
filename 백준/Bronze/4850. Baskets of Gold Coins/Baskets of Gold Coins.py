from sys import stdin, stdout


def solve():
    while True:
        try:
            n, w, d, weight = map(int, stdin.readline().rstrip().split())
            full: int = n * (n - 1) // 2 * w
            answer: int = (full - weight) // d
            if not answer:
                stdout.write("%d\n" % n)
            else:
                stdout.write("%d\n" % answer)
        except:
            break


if __name__ == "__main__":
    solve()
