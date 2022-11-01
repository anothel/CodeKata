from sys import stdin, stdout


def solution():
    nums: list = list(map(int, stdin.readline().rstrip().split(',')))
    stdout.write("%d\n" % sum(nums))


if __name__ == "__main__":
    solution()