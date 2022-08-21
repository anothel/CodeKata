from sys import stdin, stdout


def solution():
    n, m = map(int, stdin.readline().rstrip().split())
    nums: list = list()
    for _ in range(m):
        a, b = map(int, stdin.readline().rstrip().split())
        if b > a:
            nums.append(n - a)
    if len(nums) >= 1:
        nums.remove(max(nums))

    stdout.write("%d\n" % sum(nums))


if __name__ == "__main__":
    solution()
