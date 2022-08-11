from sys import stdin, stdout


def solution():
    d, m, w = map(int, stdin.readline().rstrip().split())
    i, j, k = map(int, stdin.readline().rstrip().split())

    # 한 해 전 것까지
    days: int = (k - 1) * m * d
    # 올해 것인데 오늘 것까지
    days += d * (j - 1)
    days %= w

    days += (i - 1)
    days %= w

    stdout.write("%s\n" % chr(days + 97))


if __name__ == "__main__":
    solution()
