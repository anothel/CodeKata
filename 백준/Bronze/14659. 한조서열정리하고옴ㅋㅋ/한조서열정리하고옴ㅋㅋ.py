from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    nums: list = list(map(int, stdin.readline().rstrip().split()))

    answer: int = 0

    for i in range(len(nums)):
        count: int = 0
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                count += 1
            else:
                break
        if count > answer:
            answer = count

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
