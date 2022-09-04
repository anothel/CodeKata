from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        n = int(stdin.readline().rstrip())
        nums: list = list(map(int, stdin.readline().rstrip().split()))

        stdout.write("%d\n" % (((max(nums) - sum(nums) // n) +
                                (sum(nums) // n - min(nums))) * 2))


if __name__ == "__main__":
    solution()
