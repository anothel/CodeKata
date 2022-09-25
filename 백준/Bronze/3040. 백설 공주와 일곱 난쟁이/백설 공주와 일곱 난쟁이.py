from sys import stdin, stdout
import itertools


def solution():
    nums: list = list()
    for _ in range(9):
        nums.append(int(stdin.readline().rstrip()))
    nums: list = list(itertools.permutations(nums, 7))

    for i in nums:
        if sum(i) == 100:
            for j in list(i):
                stdout.write("%d\n" % j)
            break


if __name__ == "__main__":
    solution()