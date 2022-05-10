from sys import stdin, stdout


def solve():
  for t in range(int(stdin.readline().rstrip())):
    int(stdin.readline().rstrip())
    nums: list = list(map(float, stdin.readline().rstrip().split()))
    stdout.write("%d %d\n" % (min(nums), max(nums)))


if __name__ == "__main__":
    solve()
