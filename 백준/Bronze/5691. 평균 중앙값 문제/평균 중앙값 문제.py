from sys import stdin, stdout


def solution():
    while True:
        nums: list = list(map(int, stdin.readline().rstrip().split()))

        if nums[0] == 0 and nums[1] == 0:
            break

        stdout.write("%d\n" % (nums[0] - (nums[1] - nums[0])))


if __name__ == "__main__":
    solution()