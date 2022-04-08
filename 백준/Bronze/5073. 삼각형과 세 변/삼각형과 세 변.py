from sys import stdin, stdout


def solved():
  while True:
    nums: list = sorted(map(int, stdin.readline().rstrip().split()))
    if nums[0] == 0 and nums[0] == nums[1] == nums[2]:
      return
    elif nums[2] >= nums[0] + nums[1]:
      stdout.write("Invalid \n")
    elif nums[0] == nums[1] == nums[2]:
      stdout.write("Equilateral \n")
    elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
      stdout.write("Isosceles \n")
    else:
      stdout.write("Scalene \n")


def main():
  solved()


if __name__ == "__main__":
    main()
