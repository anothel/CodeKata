from sys import stdin, stdout


def solve():
    stdout.write("Gnomes:\n")
    for _ in range(int(stdin.readline().rstrip())):
        nums: list = list(map(int, stdin.readline().rstrip().split()))
        if (nums[2] >= nums[1]
                and nums[1] >= nums[0]) or (nums[0] >= nums[1]
                                            and nums[1] >= nums[2]):
            stdout.write("Ordered\n")
        else:
            stdout.write("Unordered\n")


if __name__ == "__main__":
    solve()
