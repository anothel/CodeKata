from sys import stdin, stdout


def isAP(nums: list) -> bool:
  return True if nums[2] - nums[1] == nums[1] - nums[0] else False


def solve():
  while True:
    nums = list(map(int, stdin.readline().rstrip().split()))
    if nums[0] == 0 and nums[0] == nums[1] == nums[2]:
      break

    stdout.write(
        str("AP %d\n" % (nums[2] + (nums[1] - nums[0])) if isAP(nums) else "GP %d\n" % (nums[2] * (nums[1] / nums[0]))))


def main():
  solve()


if __name__ == "__main__":
    main()
