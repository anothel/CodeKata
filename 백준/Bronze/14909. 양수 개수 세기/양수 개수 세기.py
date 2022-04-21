from sys import stdin, stdout


def solve():
  nums: list = sorted(map(int, stdin.readline().strip().split()))

  nCount: int = 0
  for i in range(len(nums)):
    if nums[i] > 0:
      nCount += 1
  stdout.write("%d\n" % nCount)


if __name__ == "__main__":
    solve()
