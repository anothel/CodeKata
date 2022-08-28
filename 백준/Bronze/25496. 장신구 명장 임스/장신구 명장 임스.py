from sys import stdin, stdout


def solution():
    p, n = map(int, stdin.readline().rstrip().split())
    nums: list = sorted(map(int, stdin.readline().rstrip().split()))
    answer: int = 0

    for i in range(len(nums)):
        if answer >= n:
            break
        if p + nums[i] < 200:
            p += nums[i]
            answer += 1
        else:
            if p != 200:
              answer += 1
            break

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
