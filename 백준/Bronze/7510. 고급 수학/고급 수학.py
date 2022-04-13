from sys import stdin, stdout
import math


def solution():
  for i in range(1, int(stdin.readline().rstrip()) + 1):
    stdout.write("Scenario #%d:\n" % i)
    nums = sorted(map(int, stdin.readline().rstrip().split()))
    stdout.write("yes"if math.pow(
        nums[0], 2) + math.pow(nums[1], 2) == math.pow(nums[2], 2) else "no")
    stdout.write("\n\n")


def main():
  solution()


if __name__ == "__main__":
    main()
