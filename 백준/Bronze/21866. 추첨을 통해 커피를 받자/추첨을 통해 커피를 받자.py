from sys import stdin, stdout


def solve():
  nums: list = list(map(int, stdin.readline().rstrip().split()))
  if nums[0] > 100 or nums[1] > 100 or nums[2] > 200 or nums[3] > 200 or nums[4] > 300 or nums[5] > 300 or nums[6] > 400 or nums[7] > 400 or nums[8] > 500:
    stdout.write("hacker\n")
  elif sum(nums) >= 100:
    stdout.write("draw\n")
  else:
    stdout.write("none\n")


if __name__ == "__main__":
    solve()
