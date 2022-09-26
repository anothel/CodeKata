from sys import stdin, stdout
import itertools


def solution():
    n, k = map(int, stdin.readline().rstrip().split())
    nums: list = list()
    for i in range(n):
        nums.append(int(stdin.readline().rstrip()))

    answer: int = 0
    for i in reversed(range(n)):
        answer += k // nums[i]
        k %= nums[i]

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()