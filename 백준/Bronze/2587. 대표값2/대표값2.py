from sys import stdin, stdout


def solution():
    nums: list = list()
    for _ in range(5):
      nums.append(int(stdin.readline().rstrip()))
    nums.sort()
    stdout.write("%d\n" % (sum(nums) // len(nums)))
    stdout.write("%d\n" % nums[2])


if __name__ == "__main__":
    solution()
