from sys import stdin, stdout


def solution():
    while True:
        nums: list = list(map(str, stdin.readline().rstrip().split()))
        if len(nums) == 1 and nums[0] == '#':
            break
        tmp: list = nums[1:]

        answer: int = 0
        for s in tmp:
            for ss in s:
                if ss.lower() == nums[0].lower():
                    answer += 1
        stdout.write("%s %d\n" % (nums[0], answer))


if __name__ == "__main__":
    solution()