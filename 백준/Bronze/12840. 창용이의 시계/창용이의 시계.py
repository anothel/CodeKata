from sys import stdin, stdout


def solve():
    h, m, s = map(int, stdin.readline().rstrip().split())
    currentSecond: int = h * 3600 + m * 60 + s

    for i in range(int(stdin.readline().rstrip())):
        nums: list = list(map(int, stdin.readline().rstrip().split()))

        if nums[0] == 1:
            currentSecond += nums[1]
        elif nums[0] == 2:
            currentSecond -= nums[1]
        elif nums[0] == 3:
            currentSecond %= 86400
            stdout.write("%d %d %d\n" % (currentSecond // 3600,
                                         (currentSecond % 3600) // 60,
                                         (currentSecond % 60) % 60))


if __name__ == "__main__":
    solve()
