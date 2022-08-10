from sys import stdin, stdout


def solution():
    n, m, k = map(int, stdin.readline().rstrip().split())
    nums: list = [0] * n

    nums[m - 1] = 3
    tmp: int = m - 2
    while tmp >= 0:
        nums[tmp] = nums[tmp + 1] - 1
        tmp -= 1
    tmp: int = m
    while tmp <= n - 1:
        nums[tmp] = nums[tmp - 1] + 1
        tmp += 1

    x: int = k
    while True:
        if min(nums) <= x and x <= max(nums):
            break
        if x < min(nums):
            x += n
        elif max(nums) < x:
            x -= n

    stdout.write("%d\n" % (nums.index(x) + 1))


if __name__ == "__main__":
    solution()
