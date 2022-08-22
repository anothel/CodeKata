from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    nums1: list = list(map(int, stdin.readline().rstrip().split()))
    nums2: list = list(map(int, stdin.readline().rstrip().split()))

    answer: int = 0
    for i in nums1:
        answer += abs(i)
    for i in nums2:
        answer += abs(i)

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
