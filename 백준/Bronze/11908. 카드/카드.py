from sys import stdin, stdout


def solve():
    n: int = int(stdin.readline().rstrip())
    nums: list = list(map(int, stdin.readline().rstrip().split()))
    stdout.write("%d\n" % (sum(nums) - max(nums)))


if __name__ == "__main__":
    solve()
