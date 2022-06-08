from sys import stdin, stdout


def solve():
  n = int(stdin.readline().rstrip())
  nums = list(map(int, stdin.readline().rstrip().split()))

  stdout.write("%d\n" % nums.count(int(stdin.readline().rstrip())))


if __name__ == "__main__":
    solve()
