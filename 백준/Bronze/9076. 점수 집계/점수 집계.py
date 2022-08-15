from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        nums: list = list(map(int, stdin.readline().rstrip().split()))
        maxnum: int = max(nums)
        minnum: int = min(nums)
        nums.remove(maxnum)
        nums.remove(minnum)

        if max(nums) - min(nums) >= 4:
            stdout.write("KIN\n")
        else:
            stdout.write("%d\n" % sum(nums))


if __name__ == "__main__":
    solution()
