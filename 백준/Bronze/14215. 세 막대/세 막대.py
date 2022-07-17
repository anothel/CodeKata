from sys import stdin, stdout


def solve():
    nums: list = sorted(map(int, stdin.readline().rstrip().split()))
    while True:
        if nums[2] < nums[0] + nums[1]:
            break
        else:
            nums[2] -= 1
    stdout.write("%d\n" % sum(nums))


if __name__ == "__main__":
    solve()
