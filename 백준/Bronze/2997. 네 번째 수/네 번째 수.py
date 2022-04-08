from sys import stdin, stdout


def solve():
  nums: list = sorted(map(int, stdin.readline().rstrip().split()))

  if nums[2] - nums[1] == nums[1] - nums[0]:
    d: int = nums[1] - nums[0]
    stdout.write(str(nums[2] + d))
  elif nums[2] == nums[0] + 3 * (nums[1] - nums[0]):
    d: int = nums[1] - nums[0]
    stdout.write(str(nums[0] + 2 * d))
  elif nums[0] + 3 * (nums[2] - nums[1]) == nums[2]:
    d: int = nums[2] - nums[1]
    stdout.write(str(nums[0] + d))
  else:
    stdout.write(str(nums[0] - (nums[2] - nums[1])))


def main():
  solve()


if __name__ == "__main__":
    main()
