from sys import stdin, stdout


def solution():
    a, b = map(int, stdin.readline().rstrip().split())
    nums: list = list()
    answer: int = 0
    for i in range(1, b + 1):
        for _ in range(i):
            nums.append(i)
    for j in range(a - 1, b):
        answer += nums[j]
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
