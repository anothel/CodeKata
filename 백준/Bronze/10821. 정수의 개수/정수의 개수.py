from sys import stdin, stdout


def solution():
    nums: list = list(map(str, stdin.readline().rstrip().split(',')))
    answer: int = 0
    for i in nums:
        if i.isdigit():
            answer += 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
