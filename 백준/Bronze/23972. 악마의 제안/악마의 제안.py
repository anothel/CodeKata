from sys import stdin, stdout


def solve():
    k, n = map(int, stdin.readline().rstrip().split())
    if n == 1:
        stdout.write("-1\n")
    else:
        answer: int = (n * k) // (n - 1)
        if ((n * k) % (n - 1)):
            answer += 1

        stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solve()
