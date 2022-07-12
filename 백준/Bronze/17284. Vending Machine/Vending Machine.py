from sys import stdin, stdout


def solve():
    answer: int = 5000
    nums = map(int, stdin.readline().rstrip().split())

    for i in nums:
        if i == 1:
            answer -= 500
        elif i == 2:
            answer -= 800
        elif i == 3:
            answer -= 1000

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solve()
