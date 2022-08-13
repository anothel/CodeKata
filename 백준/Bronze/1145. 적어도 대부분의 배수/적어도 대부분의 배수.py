from sys import stdin, stdout
import math
import sys


def solution():
    nums = list(map(int, stdin.readline().rstrip().split()))

    cur: int = sys.maxsize
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                tmp: int = math.lcm(nums[i], nums[j], nums[k])
                if tmp < cur:
                    cur = tmp
    stdout.write("%d\n" % cur)


if __name__ == "__main__":
    solution()
