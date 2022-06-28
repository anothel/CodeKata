from sys import stdin, stdout


def solve():
    n: int = int(stdin.readline().rstrip())
    answer: int = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if n - i - j == 0:
                answer += 1
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solve()
