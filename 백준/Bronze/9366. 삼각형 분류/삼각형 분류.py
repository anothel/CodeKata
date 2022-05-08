from sys import stdin, stdout


def solve():
  for i in range(int(stdin.readline().rstrip())):
    nums: list = sorted(map(int, stdin.readline().rstrip().split()))
    stdout.write("Case #%d: " % (i + 1))
    if nums[0] == nums[1] == nums[2]:
      stdout.write("equilateral\n")
    elif nums[0] + nums[1] <= nums[2]:
      stdout.write("invalid!\n")
    elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
      stdout.write("isosceles\n")
    else:
      stdout.write("scalene\n")


if __name__ == "__main__":
    solve()
