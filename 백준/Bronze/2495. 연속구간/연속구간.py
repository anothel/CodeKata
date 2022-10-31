from sys import stdin, stdout


def solution():
    for _ in range(3):
        nums: list = list(stdin.readline().rstrip())
        before: int = nums[0]
        maxT: int = 0
        count: int = 1
        for i in nums[1:]:
            if before == i:
                count += 1
            else:
                maxT = max(maxT, count)
                before = i
                count = 1
        maxT = max(maxT, count)

        stdout.write("%d\n" % maxT)


if __name__ == "__main__":
    solution()