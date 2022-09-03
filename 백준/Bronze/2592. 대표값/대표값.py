from sys import stdin, stdout


def solution():
    sum: int = 0
    nums: list = [0 for _ in range(1001)]
    for _ in range(10):
        n: int = int(stdin.readline().rstrip())
        sum += n
        nums[n] += 1

    stdout.write("%d\n" % (sum // 10))
    stdout.write("%d\n" % (nums.index(max(nums))))


if __name__ == "__main__":
    solution()
