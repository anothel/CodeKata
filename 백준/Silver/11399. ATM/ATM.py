from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    nums: list = sorted(map(int, stdin.readline().rstrip().split()))

    answer: int = 0

    for i in range(len(nums)):
        for j in range(i + 1):
            answer += nums[j]
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
